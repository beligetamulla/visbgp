import sys
import time
from influxdb import InfluxDBClient
from multiprocessing import cpu_count
from pathlib import Path
from bgpy.simulation_framework import Simulation, ScenarioConfig
from bgpy.simulation_framework.scenarios.hijack_scenarios.prefix_hijack import PrefixHijack
from bgpy.simulation_engine.policies.bgp import BGP

class AdoptBGP(BGP):
    name = "AdoptBGP"

def main():
    # Set up InfluxDB client
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('bgpy_database')

    sim = Simulation(
        percent_adoptions=(
            0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
        ),
        scenario_configs=(
            ScenarioConfig(
                ScenarioCls=PrefixHijack,
                AdoptPolicyCls=AdoptBGP,
                BasePolicyCls=BGP,
            ),
        ),
        output_dir=Path("~/Desktop/bgpytografana2").expanduser(),
        num_trials=10,
        parse_cpus=2,
    )

    try:
        print("Running simulation...")
        results = sim.run()
        print("Simulation run completed.")

        if results is None:
            print("Simulation did not return any results.")
            return
        elif len(results) == 0:
            print("Simulation returned an empty results list.")
            return
        else:
            print(f"Simulation returned {len(results)} results.")

        for result in results:
            print("Processing result:", result)
            data_point = {
                "measurement": "bgp_hijack",
                "tags": {
                    "scenario": "PrefixHijack",
                    "adoption_rate": result.get("percent_adopt"),
                    "policy": result.get("PolicyCls"),
                },
                "time": int(time.time() * 1000),  # Current time in milliseconds
                "fields": {
                    "attacker_success": result.get("ATTACKER_SUCCESS", 0),
                    "victim_success": result.get("VICTIM_SUCCESS", 0),
                    "disconnected": result.get("DISCONNECTED", 0),
                }
            }
            client.write_points([data_point])
        print("Data written to InfluxDB successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
