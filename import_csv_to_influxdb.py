import csv
from influxdb import InfluxDBClient

# InfluxDB connection details
host = 'localhost'
port = 8086
username = 'root'
password = 'root'
dbname = 'bgpydata'

# Connect to InfluxDB
client = InfluxDBClient(host, port, username, password, dbname)

# Read CSV file
csv_file = '/root/Desktop/bgpytografana/data.csv'  # Update the path to your CSV file

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    data_points = []

    for row in csv_reader:
        data_point = {
            "measurement": "bgpy_results",
            "tags": {
                "scenario_cls": row['scenario_cls'],
                "AdoptingPolicyCls": row['AdoptingPolicyCls'],
                "BasePolicyCls": row['BasePolicyCls'],
                "PolicyCls": row['PolicyCls'],
                "outcome_type": row['outcome_type'],
                "as_group": row['as_group'],
                "outcome": row['outcome'],
                "scenario_config_label": row['scenario_config_label'],
                "scenario_label": row['scenario_label']
            },
            "fields": {
                "percent_adopt": float(row['percent_adopt']),
                "propagation_round": int(row['propagation_round']),
                "value": float(row['value']),
                "yerr": float(row['yerr'])
            }
        }
        data_points.append(data_point)

    # Write data to InfluxDB
    client.write_points(data_points)

print("Data imported successfully")
