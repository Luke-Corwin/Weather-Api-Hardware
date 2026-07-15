import network
import urequests
from machine import Pin, I2C
import ssd1306
import time
 
# Config
WIFI_SSID = "Niwroc27"
WIFI_PASS = "Liberty4All!"
API_KEY   = "f4b576c9f1436c721a794a59c862f415"
CITY      = "New York"   # change to your city
UNITS     = "imperial"
 
#OLED setup
i2c  = I2C(0, sda=Pin(4), scl=Pin(2), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
 
#Display helper
def show(l1="", l2="", l3="", l4=""):
    oled.fill(0)
    oled.text(l1[:16], 0, 0)
    oled.text(l2[:16], 0, 16)
    oled.text(l3[:16], 0, 32)
    oled.text(l4[:16], 0, 48)
    oled.show()
 
#Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    show("Connecting...", "WiFi: " + WIFI_SSID[:10])
    for _ in range(20):
        if wlan.isconnected():
            break
        time.sleep(0.5)
    if wlan.isconnected():
        show("WiFi connected!", wlan.ifconfig()[0])
        time.sleep(1)
        return True
    show("WiFi failed", "Check SSID/PASS")
    return False
 
#Fetch weather
def get_weather():
    url = ("http://api.openweathermap.org/data/2.5/weather"
           "?q=" + CITY +
           "&appid=" + API_KEY +
           "&units=" + UNITS)
    try:
        r    = urequests.get(url)
        data = r.json()
        r.close()
        temp     = round(data['main']['temp'])
        humidity = data['main']['humidity']
        feels    = round(data['main']['feels_like'])
        desc     = data['weather'][0]['description']
        return temp, humidity, feels, desc
    except Exception as e:
        print("Fetch error:", e)
        return None
 
#Weather display
def show_weather(temp, humidity, feels, desc):
    unit = "F" if UNITS == "imperial" else "C"
    show(
        CITY[:16],
        desc[:16],
        "Temp: " + str(temp) + unit,
        "Humi: " + str(humidity) + "%"
    )
    print(CITY + " | " + str(temp) + unit + " | " + str(humidity) + "% | " + desc)
 
#Main
show("Weather Station", "Starting up...")
time.sleep(1)
 
if connect_wifi():
    while True:
        result = get_weather()
        if result:
            show_weather(*result)
        else:
            show("Fetch failed", "Retrying in 30s")
        time.sleep(30)   # update every 30 seconds