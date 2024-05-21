import sys
sys.path.append('/bgpygrafana/bgpy_pkg')

from multiprocessing import cpu_count
from pathlib import Path
from frozendict import frozendict
from bgpy.simulation_framework import Simulation, ScenarioConfig
from concrete_prefix_hijack import ConcretePrefixHijack
from bgpy.simulation_engine.policies.bgp import BGP
from bgpy.as_graphs.small_as_graph_constructor import SmallASGraphConstructor

class AdoptBGP(BGP):
    name = "AdoptBGP"

def main():
    sim = Simulation(
        percent_adoptions=(0.5,),  # Test with only one percentage adoption
        scenario_configs=(
            ScenarioConfig(
                ScenarioCls=ConcretePrefixHijack,
                AdoptPolicyCls=AdoptBGP,
                BasePolicyCls=BGP,  # Ensure BasePolicyCls is set
            ),
        ),
        output_dir=Path("~/Desktop/bgpytografana").expanduser(),
        num_trials=5,  # Reduce to only one trial for quick testing
        parse_cpus=1,  # Limit to one CPU to reduce resource usage
        ASGraphConstructorCls=SmallASGraphConstructor,  # Use a smaller AS graph constructor
        as_graph_constructor_kwargs=frozendict(
            {
                "as_graph_collector_kwargs": frozendict({"cache_dir": Path("/tmp/as_graph_collector_cache")}),
                "as_graph_kwargs": frozendict({"customer_cones": True}),
                "tsv_path": None,  # Path to CAIDA TSV file if needed
            }
        ),
    )
    print("Simulation Configuration:", sim)
    sim.run()

if __name__ == "__main__":
    main()
