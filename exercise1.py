
# the umqtt module provides most of the features we need in order to use MQTT
from umqtt.simple import MQTTClient


MQTTSERVER = "server address"   # TODO enter the address of the MQTT server, as a string

# the MQTT server needs a unique ID to recognised each device that connects to it
ID = b"a unique id" # TODO create a unique id

# create a client instance
client = MQTTClient(client_id=ID, server=MQTTSERVER)

# connect to MQTT server
print("Connecting to {}".format(MQTTSERVER))
client.connect()

# messages are published to a topic
topic = b"mqtt-lab/exercise-1"

# payload content to published as part of the message.
# umqtt module can only publish strings (or byte strings).
message_content = b"message needs to be a string"   # TODO create a message to send

client.publish(topic, message_content)
print("Message published to topic {}".format(topic))

# if we aren't going to send any more messages, we should disconnect from the
# MQTT server
client.disconnect()
