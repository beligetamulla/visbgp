from bgpy.simulation_framework.scenarios.hijack_scenarios.prefix_hijack import PrefixHijack
from bgpy.simulation_engine.announcement import Announcement

class ConcretePrefixHijack(PrefixHijack):
    def _get_announcements(self, *args, **kwargs):
        # Ensure ASNs match those in the small AS graph
        return (
            Announcement(
                prefix="1.1.1.0/24",
                as_path=(12345, 67890),
                next_hop_asn=12345,
                seed_asn=12345,
                timestamp=1627281992,
            ),
            Announcement(
                prefix="2.2.2.0/24",
                as_path=(23456, 78901),
                next_hop_asn=23456,
                seed_asn=23456,
                timestamp=1627282992,
            ),
            Announcement(
                prefix="3.3.3.0/24",
                as_path=(12345, 67890),
                next_hop_asn=12345,
                seed_asn=12345,
                timestamp=1627283992,
            ),
            Announcement(
                prefix="4.4.4.0/24",
                as_path=(23456, 78901),
                next_hop_asn=23456,
                seed_asn=23456,
                timestamp=1627284992,
            ),
            Announcement(
                prefix="5.5.5.0/24",
                as_path=(12345, 67890),
                next_hop_asn=12345,
                seed_asn=12345,
                timestamp=1627285992,
            ),
        )
