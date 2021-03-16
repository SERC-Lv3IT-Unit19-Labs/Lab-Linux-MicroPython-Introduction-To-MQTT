# Lab Exercises - Introduction to MQTT

This lab will cover an introduction to using MQTT with MicroPython.

In this lab, you will:

- Connect to a MQTT server
- Publish messages to a MQTT server
- Subscribe to messages from an MQTT server

## MQTT

MQTT (MQ Telemetry Transport) is a lightweight publish/subscribe messaging protocol. Devices publish and subscribe to topics. Topics are hierarchical.

## Setup

### Install Micropython

Micropython needs to be installed onto the Ubuntu 20.04 host. Run the following command in a terminal:

```bash
sudo apt install -y micropython
```

### Configure path to 'lib' modules

The `./lib` folder needs to be added to the micropython path (so that micropython can find the files in the folder). On a microcontroller, this directory is automatically added, but on Linux it needs to be added manually.

Enter the following into a terminal:

```bash
MICROPYPATH=$MICROPYPATH:"./lib"
```

To check that you have added `./lib` correctly to `MICROPYPATH` enter the following command into a terminal:

```bash
echo $MICROPYPATH
```

The output should be similar to:

```bash
:./lib
```


## Exercise 1 - Connecting to a MQTT server

In this exercise, you will connect to an MQTT server.

Open the `exercise1.py` file. The script follows the following pattern, which is typical for basic MQTT operations.

- import the umqtt module
- create an instance of the MQTT client
- connect to a MQTT server
- publish a message
- disconnect from server

Complete the following tasks.

### Tasks

1. Replace the `MQTTSERVER` address with the IP address of the MQTT server you are connecting to. (Your instructor will give you an address.)

1. Replace the `ID` with a unique device ID. The MQTT server will use this ID to identify each device that connects to it.

1. Replace the `message_content` with a message of your own.

1. Run the file. To run the file, enter the following into a terminal:

    ```bash
    micropython exercise1.py
    ```

    Observe the output from the file. Check that there are no error messages.

    Look in MQTT Explorer and try to find your message.

1. Try entering different messages and run the file again. Check MQTT Explorer each time and try to find your message.


Q. How could you make it easier to find your message amoung everyone else's messages?

<br />

## Exercise 2 - Publish messages

In this exercise you will simulate readings from a temperature sensor and send those readings to an MQTT topic.

Open the `exercise2.py` file. This file uses the `simulated_sensor` module to create a simulated temperature sensor. The sensor object is created with the line

```python
sensor = simulated_sensor.TemperatureSensor(SENSORPIN)
```

A temperature reading is created with the method `read_temperature()`. You can see this with line 37.

```python
temp = sensor.read_temperature()
```

### Tasks

1. As in Exercise 1, replace the `MQTTSERVER` address with the IP address of the MQTT server and replace the `ID` with a unique device ID.

1. On line 29, create a sub-topic just for your sensor. Use a suitable name for the subtopic.

1. Run the file.

    ```bash
    micropython exercise2.py
    ```

    Observe the output from the file. Check that there are no error messages.

    Leave the file running and observe the messages in MQTT Explorer.


Q. How would you increase or decrease the frequency of readings and messages?

### Additional Tasks

In these additional tasks you will change the simulated temperature sensor to a temperature and humidity sensor. This will produce two readings; one for temperature and one for humidity. You will publish temperature and humidity on seperate subtopics.

1. Replace `TemperatureSensor` on line 19 with `TempHumSensor` as such

    ```python
    sensor = simulated_sensor.TempHumSensor(SENSORPIN)
    ```

1. The humidity can be read using the method `read_humidity()`. Create a variable to hold the humidity reading and use the `read_humidity()` method to take a reading. (If you are unsure how to do this, look at line 37 at how the temperature is read. Reading humidity will be similar.) You can also modify the print statement to include the humidity reading along side the temperature reading.

1. Add an additional publish command to publish the humidity reading to the MQTT server. You will need to make further modifications to the code so that temperature and humidity publish to seperate suitable subtopics. Both readings still need to be identifiable as coming from your sensor.

1. When you have made the necessary changes, run the file.

    ```bash
    micropython exercise2.py
    ```

    Observe the output from the file. Check that there are no error messages.

    Leave the file running and observe the messages in MQTT Explorer.

Q. Is it easy to navigate and observe everyone else's sensor readings? What could be done to make it easier to navigate the other sensor readings?

<br />

## Exercise 3 - Subscribe to topics

In this exercise, you will subscribe to topics and receive messages from an MQTT server. We will create and run a very crude and basic messaging app.

Open both `exercise3receive.py` and `exercise3send.py` files.

### Tasks
 
1. As with previous exercises, in both files, replace the `MQTTSERVER` address with the IP address of the MQTT server and replace the `ID` with a unique device ID.

1. When you have made the necessary changes, create a split terminal in VSCode and run each file in a seperate terminal run the file.

    Run the following in one terminal:

    ```bash
    micropython exercise3receive.py
    ```

    and the following in the other:

    ```bash
    micropython exercise3send.py
    ```

    Observe the output from each file. Check that there are no error messages.

    Type some messages in the `exercise3send.py` script. Notice that you get your message back in the `exercise3receive.py` script terminal, as well as everyone else's messages.

    Q. How could you narrow down who you get messages from?

1. In `exercise3receive.py`, change the subscribe subtopic so that people can send messages to just you.

1. In `exercise3send.py`, change the publish subtopic to match someone else's subsribe topic. Try sending some messages to that person.

<br />

## Conclusion

In this lab, you:

- connected to an MQTT server
- published messages to a MQTT topic
- subscribed to and recieved messages from a MQTT topic
