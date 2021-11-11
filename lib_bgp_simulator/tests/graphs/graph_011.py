from pathlib import Path

from lib_caida_collector import PeerLink, CustomerProviderLink as CPLink

from .graph_info import GraphInfo
from ...enums import ASNs


class Graph011(GraphInfo):
    r"""
    TODO: Add reference to image online (it's a bit much for pixel art)
    """
    def __init__(self):
        super(Graph011, self).__init__(
            peer_links=set([
                PeerLink(9, 8),
                PeerLink(1, 2),
                PeerLink(2, 3)
            ]),
            customer_provider_links=set([
                CPLink(provider_asn=4,customer_asn=5),
                CPLink(provider_asn=4,customer_asn=7),
                CPLink(provider_asn=5,customer_asn=6),
                CPLink(provider_asn=7,customer_asn=8),
                CPLink(provider_asn=8,customer_asn=3),
                CPLink(provider_asn=9,customer_asn=1),
                CPLink(provider_asn=1,customer_asn=5),
                CPLink(provider_asn=2,customer_asn=11),
                CPLink(provider_asn=11,customer_asn=12),
                CPLink(provider_asn=12,customer_asn=ASNs.VICTIM.value),
                CPLink(provider_asn=3,customer_asn=ASNs.ATTACKER.value)
            ])
    )
