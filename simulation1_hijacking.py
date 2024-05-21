import sys
sys.path.append('/bgpygrafana/bgpy_pkg')

from multiprocessing import cpu_count
from pathlib import Path
from bgpy.simulation_framework import Simulation, ScenarioConfig
from bgpy.simulation_framework.scenarios.hijack_scenarios.prefix_hijack import PrefixHijack
from bgpy.simulation_engine.policies.bgp import BGP

class AdoptBGP(BGP):
    name = "AdoptBGP"

def main():
    sim = Simulation(
        percent_adoptions=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9),
        scenario_configs=(
            ScenarioConfig(
                ScenarioCls=PrefixHijack,
                AdoptPolicyCls=AdoptBGP,
                BasePolicyCls=BGP,
            ),
        ),
        output_dir=Path("~/Desktop/bgpytografana1").expanduser(),
        num_trials=20,
        parse_cpus=cpu_count(),
    )
    sim.run()

if __name__ == "__main__":
    main()
