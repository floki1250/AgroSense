import dht
import machine
import network
import urequests
import utime

# Set up the DHT22 sensor
dht_pin = machine.Pin(14, machine.Pin.IN)
dht_sensor = dht.DHT22(dht_pin)

# Set up the Firebase Realtime Database
firebase_url = "https://your-project.firebaseio.com/"
firebase_auth = "your-auth-token"
firebase_path = "sensor-data"

# Connect to Wi-Fi
ssid = "your-wifi-ssid"
password = "your-wifi-password"
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)
while not sta_if.isconnected():
    utime.sleep(1)

# Read data from the DHT22 sensor
dht_sensor.measure()
temperature = dht_sensor.temperature()
humidity = dht_sensor.humidity()

# Send data to Firebase
data = {"temperature": temperature, "humidity": humidity}
firebase_url += firebase_path + ".json?auth=" + firebase_auth
response = urequests.post(firebase_url, json=data)

# Print the server response
print(response.status_code, response.text)
