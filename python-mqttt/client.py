import paho.mqtt.client as mqtt
import time


# Define the callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker via WebSocket")
        # Subscribe to a topic upon successful connection
        client.subscribe("test/websocket/topic")
    else:
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    # Print the message received from the broker
    print(f"Received message: {msg.topic} -> {msg.payload.decode()}")


def on_publish(client, userdata, mid):
    print(f"Message {mid} published successfully")


def on_disconnect(client, userdata, rc):
    print("Disconnected from broker")


# Create a client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, transport="websockets")
client.tls_set()
# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Set the WebSocket path (optional for some brokers)
# For example, if the broker needs a specific WebSocket URL path:
client.ws_set_options(path="/mqtt")

# Connect to an MQTT broker using WebSockets
broker = "iot-mqtt-broker.click"  # WebSocket-enabled broker address
port = 443  # Common WebSocket port for Mosquitto

print(f"Connecting to broker {broker} on port {port} via WebSocket")
client.username_pw_set("hass", "anhquan2014")

client.connect(broker, port, 30)

# Start the network loop in a non-blocking way
client.loop_start()

# Publish a message to the WebSocket topic
topic = "test/websocket/topic"
message = "Hello, MQTT over WebSocket!"


# Keep the client running for some time to allow message exchange
try:
    while True:
        client.publish(topic, message)
        time.sleep(2)
        pass  # Add your application logic here
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    client.disconnect()
