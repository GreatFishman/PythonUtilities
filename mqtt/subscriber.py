import paho.mqtt.client as mqtt

server_ip = "127.0.0.1"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print (msg.topic+ " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server_ip, 1883, 60)


client.loop_forever()