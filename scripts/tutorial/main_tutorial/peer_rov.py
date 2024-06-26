from bgpy.simulation_engine import Announcement as Ann
from bgpy.simulation_engine import BGP
from bgpy.enums import Relationships


class PeerROV(BGP):
    """An Policy that deploys PeerROV"""

    name: str = "TutorialPeerROV"

    # mypy doesn't understand that this func is valid
    def _valid_ann(self, ann: Ann, *args, **kwargs) -> bool:  # type: ignore
        """Returns announcement validity

        Returns false if invalid by roa and coming from a peer,
        otherwise uses standard BGP (such as no loops, etc)
        to determine validity
        """

        # Invalid by ROA is not valid by ROV
        # Since this type of real world ROV only does peer filtering, only peers here
        if ann.invalid_by_roa and ann.recv_relationship == Relationships.PEERS:
            return False
        # Use standard BGP to determine if the announcement is valid
        else:
            # Mypy doesn't map superclasses properly
            return super(PeerROV, self)._valid_ann(ann, *args, **kwargs)  # type: ignore
