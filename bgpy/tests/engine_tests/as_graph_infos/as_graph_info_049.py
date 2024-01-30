from bgpy.as_graphs import PeerLink, CustomerProviderLink as CPLink

from bgpy.as_graphs import ASGraphInfo
from bgpy.enums import ASNs


as_graph_info_049 = ASGraphInfo(
    peer_links=frozenset([PeerLink(1, 2)]),
    customer_provider_links=frozenset(
        [
            CPLink(provider_asn=4, customer_asn=3),
            CPLink(provider_asn=4, customer_asn=7),
            CPLink(provider_asn=3, customer_asn=1),
            CPLink(provider_asn=3, customer_asn=2),
            CPLink(provider_asn=1, customer_asn=ASNs.ATTACKER.value),
            CPLink(provider_asn=2, customer_asn=5),
            CPLink(provider_asn=5, customer_asn=6),
            CPLink(provider_asn=6, customer_asn=7),
            CPLink(provider_asn=7, customer_asn=8),
            CPLink(provider_asn=7, customer_asn=9),
        ]
    ),
)