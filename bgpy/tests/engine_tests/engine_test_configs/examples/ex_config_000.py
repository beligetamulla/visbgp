from frozendict import frozendict
from bgpy.enums import ASNs
from bgpy.tests.engine_tests.as_graph_infos import as_graph_info_000
from bgpy.tests.engine_tests.utils import EngineTestConfig

from bgpy.simulation_engine import (
    BGPSimplePolicy,
    ROVSimplePolicy,
)
from bgpy.simulation_framework import (
    ScenarioConfig,
    ValidPrefix,
)


desc = (
    "Valid prefix with BGP Simple"
)

ex_config_000 = EngineTestConfig(
    name="ex_000_valid_prefix_bgp_simple",
    desc=desc,
    scenario_config=ScenarioConfig(
        ScenarioCls=ValidPrefix,
        BasePolicyCls=BGPSimplePolicy,
        override_attacker_asns=frozenset(),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict(),
    ),
    as_graph_info=as_graph_info_000,
)
