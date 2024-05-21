from bgpy.as_graphs.base import ASGraphConstructor
from bgpy.as_graphs.caida_as_graph import CAIDAASGraph, CAIDAASGraphCollector

class SmallASGraphConstructor(ASGraphConstructor):
    def __init__(self, **kwargs):
        super().__init__(ASGraphCollectorCls=CAIDAASGraphCollector, ASGraphCls=CAIDAASGraph, **kwargs)

    def _get_as_graph_info(self, dl_path=None):
        # Manually create a small AS graph info
        as_graph_info = {
            "nodes": {
                1: {"degree": 1, "type": "stub"},
                2: {"degree": 2, "type": "transit"},
                3: {"degree": 1, "type": "stub"},
            },
            "edges": [
                {"from": 1, "to": 2, "type": "provider_customer"},
                {"from": 2, "to": 3, "type": "provider_customer"},
            ],
            "ixp_asns": set(),  # Ensure ixp_asns is included
            "as_rel_dict": {},  # Example additional attribute if needed
        }
        return as_graph_info

    def _get_as_graph(self, as_graph_info):
        # Ensure the dictionary contains the required attributes
        if "ixp_asns" not in as_graph_info:
            as_graph_info["ixp_asns"] = set()
        if "as_rel_dict" not in as_graph_info:
            as_graph_info["as_rel_dict"] = {}
        return CAIDAASGraph(as_graph_info)
