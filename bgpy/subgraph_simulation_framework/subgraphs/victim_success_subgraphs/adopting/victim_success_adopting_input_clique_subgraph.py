from ..victim_success_subgraph import VictimSuccessSubgraph
from .....enums import ASGroups
from .....enums import Outcomes
from ....scenarios import Scenario


class VictimSuccessAdoptingInputCliqueSubgraph(VictimSuccessSubgraph):
    """Graph with attacker success for adopting input clique ASes"""

    name: str = "victim_success_adopting_input_clique"

    def _get_subgraph_key(self, scenario: Scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASGroups.INPUT_CLIQUE, scenario.AdoptASCls, Outcomes.VICTIM_SUCCESS
        )