import requests
from plyer import notification
import time


API_KEY = "Your own Api key from any weather notifying website"  
CITY = "Mumbai"                          
CHECK_INTERVAL = 60                       


def get_weather():
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "error" in data:
        print("Error fetching weather data:", data)
        return None

    weather = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]
    return weather, temp_c

def send_notification(weather, temp):
    title = f"🌡️ Temperature in {CITY}"
    message = f"Condition: {weather}\nTemp: {temp}°C"

    notification.notify(
        title=title,
        message=message,
        timeout=10
    )


print(f"Running temperature notifier for {CITY} every {CHECK_INTERVAL // 60} minutes...")

while True:
    print(f"Checking weather now for {CITY}...")  
    result = get_weather()
    if result:
        weather, temp = result
        send_notification(weather, temp)
    time.sleep(CHECK_INTERVAL)
