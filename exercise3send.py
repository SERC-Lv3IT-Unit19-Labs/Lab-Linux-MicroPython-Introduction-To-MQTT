
from umqtt.simple import MQTTClient


MQTTSERVER = "server address"   # TODO enter the address of the MQTT server, as a string

# the MQTT server needs a unique ID to recognised each device that connects to it
ID = b"send" + b"a unique id" # TODO create a unique id

# use a base topic to group messages into a common hierarchy
BASE_TOPIC = b"mqtt-lab/exercise-3"

# topic to send messages to
publish_topic = BASE_TOPIC + b"/my-messages"  # TODO change the subtopic to a topic that others can message your on


try:
    # create a client instance
    client = MQTTClient(client_id=ID, server=MQTTSERVER)

    # connect to MQTT server
    print("Connecting to {}".format(MQTTSERVER))
    client.connect()

    # send diagnostic message to server
    connect_message = b"Connected from sender: " + ID
    client.publish(BASE_TOPIC, connect_message)

    print("Message receiver started. Sending messages to {}".format(publish_topic))
    print("Press Ctrl + c to exit.")
    print()

    while True:
        message = input("Enter a message to send: ")

        client.publish(publish_topic, message)


except KeyboardInterrupt:
    client.disconnect()
    print("\nProgram terminated by user.")
    print("Goodbye")
