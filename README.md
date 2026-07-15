# ESP32 Weather Station

Fetches live weather data from OpenWeatherMap via WiFi and displays current temperature, humidity, and conditions on an SSD1306 OLED screen. Refreshes every 30 seconds.

## Parts
- ESP32 dev board
- SSD1306 OLED display (0.96", I2C, 128x64)
- Jumper wires + breadboard

## Wiring
| OLED Pin | ESP32 Pin |
|----------|-----------|
| VCC | 3.3V |
| GND | GND |
| SDA | GPIO4 |
| SCL | GPIO2 |

## Libraries needed
- `ssd1306.py` — get it from:
  https://raw.githubusercontent.com/micropython/micropython-lib/master/micropython/drivers/display/ssd1306/ssd1306.py

Drop it onto the ESP32 via Thonny (File → Save a copy → MicroPython device).

## Setup
1. Sign up for a free API key at openweathermap.org (takes ~2 hours to activate)
2. Open `weather_config.py` and fill in your WiFi, API key, and city
3. Copy `weather_config.py`, `weather.py`, and `ssd1306.py` onto the ESP32
4. Run `weather.py` — OLED shows live weather on connect

## Config
Edit `weather_config.py` only — no need to touch `weather.py`.

```python
WIFI_SSID    = "your network"
WIFI_PASS    = "your password"
API_KEY      = "your key"
CITY         = "Chicago"        # spaces → %20 e.g. "New%20York"
UNITS        = "imperial"       # imperial = F / metric = C
UPDATE_EVERY = 30               # seconds between refreshes
```

## Notes
- City names with spaces must use %20 (e.g. "New%20York")
- API key takes up to 2 hours to activate after creation
- If import urequests fails: run `import mip; mip.install('urequests')` in Thonny shell
- OLED default I2C address is 0x3C
