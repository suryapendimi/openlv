#mqqt messaging client example, Robert Brown, London South Bank University, 27.06.2018

#set mqtt server and topic parameters
broker_address="broker.hivemq.com" #for TESTING only - see www.mqtt-dashboard.com
topic = "orxa/openlv/test1"


import paho.mqtt.client as mqtt
import time, datetime, random


def timestampPrint(msg):
    """prints current datetime followed by msg"""
    time_now = datetime.datetime.now()
    print(f"{time_now}: {msg}")

def msgCallback(client, userdata, message):
    """captures message from paho.mqtt.client instance on_message callback"""
    msg = message.payload.decode("utf-8")
    timestampPrint(f"new message received on topic {message.topic}:\t\"{str(msg)}\"")

def randomMessage():
    """generate a random message about feeder voltage violation"""
    feeder_no, location_no = [random.randint(1,10) for _ in range(2)]
    feeder_location = random.choice(["factory", "substation", "feeder pillar"])
    return f"voltage violation on feeder {feeder_no} at {feeder_location} {location_no}"


#set up mqtt client instance
client = mqtt.Client("orxa")
client.on_message=msgCallback 

#connect to server
client.connect(broker_address)
timestampPrint(f"connected to mqtt server at {broker_address}")
client.loop_start() #start the loop

#subscribe to topic
client.subscribe(topic)
timestampPrint(f"subcribed to topic {topic} - started listening for messages")

#publish message
msg = randomMessage()
client.publish("orxa/openlv/test1",msg)
timestampPrint(f"published message on topic {topic}:\t\"{msg}\"")

#wait for messages
timestampPrint(f"waiting 5 seconds for messages to arrive")
time.sleep(5)

#stop waiting for messages
client.loop_stop()
timestampPrint(f"stopped listening for messages\n")
