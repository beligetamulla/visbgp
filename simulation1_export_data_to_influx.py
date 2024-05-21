from influxdb import InfluxDBClient
import csv
import os
from pathlib import Path

def import_csv_to_influxdb(csv_file, db_name, measurement):
    client = InfluxDBClient(host='localhost', port=8086)
    client.create_database(db_name)
    client.switch_database(db_name)
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data_points = []
        for row in reader:
            data_point = {
                "measurement": measurement,
                "tags": {
                    "scenario_cls": row["scenario_cls"],
                    "AdoptingPolicyCls": row["AdoptingPolicyCls"],
                    "BasePolicyCls": row["BasePolicyCls"],
                    "PolicyCls": row["PolicyCls"],
                    "outcome_type": row["outcome_type"],
                    "as_group": row["as_group"]
                },
                "fields": {
                    "outcome": row["outcome"],
                    "percent_adopt": float(row["percent_adopt"]),
                    "propagation_round": int(row["propagation_round"]),
                    "value": float(row["value"]),
                    "yerr": float(row["yerr"]) if row["yerr"] else 0.0
                }
            }
            data_points.append(data_point)
        
        client.write_points(data_points)
    print("Data imported successfully")

# Replace with your CSV file path and expand user path
csv_file_path = str(Path("~/Desktop/bgpytografana1/data.csv").expanduser())
import_csv_to_influxdb(csv_file_path, "bgpy_database", "hijacking_data")
