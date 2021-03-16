#
import time
from umqtt.simple import MQTTClient
import lib.simulated_sensor as simulated_sensor

# the Linux host doesn't have pins for attaching sensors too. We are practicing
# for using microcontrollers though, so define a pretend pin.
SENSORPIN = 4

MQTTSERVER = "server address"   # TODO enter the address of the MQTT server, as a string

# the MQTT server needs a unique ID to recognised each device that connects to it
ID = b"a unique id" # TODO create a unique id

# use a base topic to group messages into a common hierarchy
BASE_TOPIC = b"mqtt-lab/exercise-2"

# create a temperature sensor instance
sensor = simulated_sensor.TemperatureSensor(SENSORPIN)

# create a client instance
client = MQTTClient(client_id=ID, server=MQTTSERVER)

# connect to MQTT server
print("Connecting to {}".format(MQTTSERVER))
client.connect()

# messages are published to a topic
topic = BASE_TOPIC + b"/my-sensor"   # TODO replace the subtopic with a subtopic to identify your sensor


print("Simulating temperature readings and sending MQTT messages.")
print("Press Ctrl + c to exit.")

try:
    while True:
        temp = sensor.read_temperature()
        print("Temperature: {0:4.2f} C. Sending message...".format(temp), end='\r')

        # publish payload to mqtt topic
        payload = str(temp)
        client.publish(topic, payload)
        
        # pause between readings
        time.sleep(5)

except KeyboardInterrupt:
    client.disconnect()
    print("\nProgram terminated by user.")
    print("Goodbye")
