from dataclasses import dataclass, asdict, replace
from typing import Any, Optional
from yamlable import YamlAble, yaml_info
from bgpy.enums import Relationships
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

@yaml_info(yaml_tag="Announcement")
@dataclass(slots=True, frozen=True)
class Announcement(YamlAble):
    """BGP Announcement"""
    prefix: str
    as_path: tuple[int, ...]
    next_hop_asn: int = None  # type: ignore
    seed_asn: Optional[int] = None
    recv_relationship: Relationships = Relationships.ORIGIN
    timestamp: int = 0
    withdraw: bool = False
    traceback_end: bool = False
    roa_valid_length: Optional[bool] = None
    roa_origin: Optional[int] = None
    bgpsec_next_asn: Optional[int] = None
    bgpsec_as_path: tuple[int, ...] = ()
    only_to_customers: Optional[int] = None

    def __post_init__(self):
        if self.seed_asn is None:
            if len(self.as_path) == 1:
                object.__setattr__(self, "seed_asn", self.as_path[0])
        if self.next_hop_asn is None:
            if len(self.as_path) == 1:  # type: ignore
                object.__setattr__(self, "next_hop_asn", self.as_path[0])
            else:
                raise ValueError("Must set next_hop_asn")

    def prefix_path_attributes_eq(self, ann: Optional["Announcement"]) -> bool:
        if ann is None:
            return False
        elif isinstance(ann, Announcement):
            return (ann.prefix, ann.as_path) == (self.prefix, self.as_path)
        else:
            raise NotImplementedError

    def copy(self, overwrite_default_kwargs: Optional[dict[Any, Any]] = None) -> "Announcement":
        kwargs = {"seed_asn": None, "traceback_end": False}
        if overwrite_default_kwargs:
            kwargs.update(overwrite_default_kwargs)
        return replace(self, **kwargs)  # type: ignore

    def bgpsec_valid(self, asn: int) -> bool:
        return self.bgpsec_next_asn == asn and self.bgpsec_as_path == self.as_path

    @property
    def invalid_by_roa(self) -> bool:
        if self.roa_origin is None:
            return False
        else:
            return self.origin != self.roa_origin or not self.roa_valid_length

    @property
    def valid_by_roa(self) -> bool:
        return bool(self.origin == self.roa_origin and self.roa_valid_length)

    @property
    def unknown_by_roa(self) -> bool:
        return not self.invalid_by_roa and not self.valid_by_roa

    @property
    def covered_by_roa(self) -> bool:
        return not self.unknown_by_roa

    @property
    def roa_routed(self) -> bool:
        return self.roa_origin != 0

    @property
    def origin(self) -> int:
        return self.as_path[-1]

    def __str__(self) -> str:
        return f"{self.prefix} {self.as_path} {self.recv_relationship}"

    def send_to_influx(self):
        client = influxdb_client.InfluxDBClient(url="http://localhost:8086")
        write_api = client.write_api(write_options=SYNCHRONOUS)
        data = {
            "measurement": "bgp_announcements",
            "tags": {
                "prefix": self.prefix,
                "as_path": ",".join(map(str, self.as_path)),
                "next_hop_asn": str(self.next_hop_asn)
            },
            "fields": {
                "origin": self.origin,
                "timestamp": self.timestamp
            }
        }
        write_api.write(bucket="bgp_data", record=data)

    def __to_yaml_dict__(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def __from_yaml_dict__(cls: type["Announcement"], dct: dict[str, Any], yaml_tag: Any) -> "Announcement":
        return cls(**dct)
