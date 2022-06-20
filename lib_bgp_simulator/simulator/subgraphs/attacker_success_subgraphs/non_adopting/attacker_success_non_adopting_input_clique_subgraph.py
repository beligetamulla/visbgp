from abc import ABC, abstractmethod
from collections import defaultdict

import ipaddress

from ..attacker_success_subgraph import AttackerSuccessSubgraph
from .....enums import Outcomes
from .....engine import BGPAS


class AttackerSuccessNonAdoptingInputCliqueSubgraph(AttackerSuccessSubgraph):
    """Graph with attacker success for non adopting input clique ASes"""

    def aggregate_engine_run_data(self,
                                  shared_data,
                                  engine,
                                  *,
                                  percent_adopt,
                                  trial,
                                  scenario,
                                  propagation_round):
        """Aggregates data after a single engine run

        Shared data is passed between subgraph classes and is
        mutable. This is done to speed up data aggregation, even
        though it is at the cost of immutability
        """

        raise NotImplementedError
