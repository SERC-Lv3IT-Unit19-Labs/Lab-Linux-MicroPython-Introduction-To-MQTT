# Lab Exercises - Introduction to MQTT

This lab will cover an introduction to using MQTT with MicroPython.

In this lab, you will:

- Connect to a MQTT server

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

