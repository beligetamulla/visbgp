from frozendict import frozendict
from bgpy.tests.engine_tests.graphs import as_graph_info_002
from bgpy.tests.engine_tests.utils import EngineTestConfig

from bgpy.simulation_engine import BGPSimplePolicy
from bgpy.enums import ASNs
from bgpy.simulation_framework import ScenarioConfig, ValidPrefix


config_003 = EngineTestConfig(
    name="003",
    desc="Basic BGP Propagation (with simple AS)",
    scenario_config=ScenarioConfig(
        ScenarioCls=ValidPrefix,
        BasePolicyCls=BGPSimplePolicy,
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict(),
    ),
    as_as_graph_info_info=as_graph_info_002,
)
