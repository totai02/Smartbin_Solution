import paho.mqtt.client as mqtt
from config import *

class MqttService:

    def __init__(self):
        self.client = mqtt.Client("P1")
        self.client.connect(BROCKER_ADDRESS) 

    def publish(self, topic, data):
        self.client.publish(topic, data)