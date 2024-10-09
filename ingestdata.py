import time
from influxdb_client import InfluxDBClient, Point, WritePrecision

# Configuration
url = "http://localhost:8086"
token = "secret_token"
org = "cost"
bucket = "ec2_bucket"

# Create a client
client = InfluxDBClient(url=url, token=token, org=org)

# Prepare a list of data to write
data_list = [
    {"sensor": "room1", "value": 23.5},
    {"sensor": "room1", "value": 24.0},
    {"sensor": "room2", "value": 22.5},
    {"sensor": "room2", "value": 21.0},
]

# Create points and write to InfluxDB
with client.write_api() as write_api:
    for data in data_list:
        # Create a point for each entry
        point = Point("temperature") \
            .tag("sensor", data["sensor"]) \
            .field("value", data["value"]) \
            .time(int(time.time() * 1_000_000_000), WritePrecision.NS)
        
        # Write the point
        write_api.write(bucket=bucket, org=org, record=point)

print("Data written to InfluxDB")
