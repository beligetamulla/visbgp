from typing import Optional, TYPE_CHECKING
from bgpy.simulation_framework.scenarios.scenario import Scenario
from bgpy.simulation_framework.scenarios.roa_info import ROAInfo
from bgpy.enums import Prefixes
from bgpy.enums import Timestamps

if TYPE_CHECKING:
    from bgpy.simulation_engine import Announcement as Ann
    from bgpy.simulation_engine import BaseSimulationEngine

class PrefixHijack(Scenario):
    """Prefix Hijack Scenario"""

    def _get_announcements(self, *args, **kwargs) -> tuple["Ann", ...]:
        anns = list()
        for victim_asn in self.victim_asns:
            anns.append(
                self.scenario_config.AnnCls(
                    prefix=Prefixes.PREFIX.value,
                    as_path=(victim_asn,),
                    timestamp=Timestamps.VICTIM.value,
                )
            )

        for attacker_asn in self.attacker_asns:
            anns.append(
                self.scenario_config.AnnCls(
                    prefix=Prefixes.PREFIX.value,
                    as_path=(attacker_asn,),
                    timestamp=Timestamps.ATTACKER.value,
                )
            )
        return tuple(anns)

    def _get_roa_infos(
        self,
        *,
        announcements: tuple["Ann", ...] = (),
        engine: Optional["BaseSimulationEngine"] = None,
        prev_scenario: Optional["Scenario"] = None,
    ) -> tuple[ROAInfo, ...]:
        err: str = "Fix the roa_origins of the " "announcements for multiple victims"
        assert len(self.victim_asns) == 1, err

        roa_origin: int = next(iter(self.victim_asns))

        return (ROAInfo(Prefixes.PREFIX.value, roa_origin),)
