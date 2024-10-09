docker exec -it influxdb influx v1 shell


docker exec -it influxdb influx v1 shell -token secret_token;

docker exec -it influxdb influx bucket create -n demo_bucket -o my_org


docker exec -it influxdb influx write --bucket demo_bucket --org my_org 'temperature,sensor=room1 value=23.5 1630350000000000000'
docker exec -it influxdb  influx write --bucket demo_bucket --org my_org 'temperature,sensor=room2 value=22.0 1630350060000000000'


docker exec -it influxdb influx query 'from(bucket: "demo_bucket") |> range(start: -1h)'


curl -G 'http://localhost:8086/api/v2/query?org=my_org&bucket=demo_bucket' \
  --header "Authorization: Token secret_token" \
  --data-urlencode 'query=from(bucket: "demo_bucket") |> range(start: 0) |> filter(fn: (r) => r._measurement == "temperature" and r.sensor == "room2")'
