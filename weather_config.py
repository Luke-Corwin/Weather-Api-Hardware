# ─────────────────────────────────────────────────────────────
#  Weather Station — Config
#  Edit this file only. No need to touch weather.py.
# ─────────────────────────────────────────────────────────────

# WiFi
WIFI_SSID = "YOUR_WIFI_NAME"
WIFI_PASS = "YOUR_WIFI_PASSWORD"

# OpenWeatherMap
API_KEY = "YOUR_API_KEY"
CITY    = "New%20York"   # spaces → %20  e.g. "Los%20Angeles"

# Units: "imperial" = Fahrenheit / "metric" = Celsius
UNITS = "imperial"

# How often to refresh in seconds (30 minimum recommended)
UPDATE_EVERY = 30

# OLED I2C pins
SDA_PIN = 4
SCL_PIN = 2
