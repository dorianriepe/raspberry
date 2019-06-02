from influxdb import InfluxDBClient
import time
import Python_DHT

sensor = Python_DHT.DHT11
pin = 4

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('dht11')

for x in range(60):

    humidity, temperature = Python_DHT.read_retry(sensor, pin)

    json_body = [
        {
            "measurement": "sensor_data",
            "tags": {
                "location": "bedroom",
            },
            "fields": {
                "temperature": temperature,
                "humidity": humidity
            }
        }
    ]

    time.sleep(30)
    client.write_points(json_body)
    print(temperature)