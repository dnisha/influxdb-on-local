from influxdb_client import InfluxDBClient

# Configuration
url = "http://localhost:8086"
token = "secret_token"
org = "cost"
bucket = "ec2_bucket"

# Create a client
client = InfluxDBClient(url=url, token=token, org=org)

# Create an instance of the QueryApi
query_api = client.query_api()

# Define the query
query = f'''
from(bucket: "{bucket}")
  |> range(start: -1w)  // Adjust the range as needed
  |> filter(fn: (r) => r._measurement == "temperature" and r.sensor == "room1")
'''

# Execute the query
results = query_api.query(query, org=org)

# Print the results
for table in results:
    for record in table.records:
        print(f'Time: {record.get_time()}, Sensor: {record["sensor"]}, Value: {record.get_value()}')

# Close the client
client.close()
