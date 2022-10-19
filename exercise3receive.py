
import time
from umqtt.simple import MQTTClient


MQTTSERVER = "server address"   # TODO enter the address of the MQTT server, as a string

# the MQTT server needs a unique ID to recognised each device that connects to it
ID = b"receive" + b"a unique id" # TODO create a unique id

# use a base topic to group messages into a common hierarchy
BASE_TOPIC = b"mqtt-lab/exercise-3"

# topic to subscribe to messages from
subscribe_topic = BASE_TOPIC + b"/my-messages"  # TODO change the subtopic to a topic that others can message you on

# mqtt message callback
# this function is called if a message is received
def mqtt_cb(topic, msg):
    print("Message received from topic: {}".format(topic))
    print(msg)
    print()



try:
    # create a client instance
    client = MQTTClient(client_id=ID, server=MQTTSERVER)

    # connect to MQTT server
    print("Connecting to {}".format(MQTTSERVER))
    client.connect()

    # send diagnostic message to server
    connect_message = b"Connected from reciever: " + ID
    client.publish(BASE_TOPIC, connect_message)

    # tell umqtt which function to use for message callbacks
    client.set_callback(mqtt_cb)

    # tell the MQTT server that you want messages from a topic
    client.subscribe(subscribe_topic)


    print("Message receiver started. Receiving messages from {}".format(subscribe_topic))
    print("Press Ctrl + c to exit.")
    print()

    while True:
        time.sleep(0.1)
        client.check_msg()

except KeyboardInterrupt:
    client.disconnect()
    print("\nProgram terminated by user.")
    print("Goodbye")
