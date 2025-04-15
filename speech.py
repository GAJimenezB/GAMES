import speech_recognition as sr
from datetime import datetime
import webbrowser
import requests


time = datetime.now().strftime("%H:%M:%S")
api_key = "7d2b62e49e8195e515fa1e3e0c4949e0"
city = "Luxembourg"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es"
response = requests.get(url)
data = response.json()

recognizer = sr.Recognizer()
mic = sr.Microphone()

if response.status_code == 200:
    temperature = data["main"]["temp"]
else:
    print(f"Error: Was nos possible to get the info of {city}.")
while(True):
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listen...speak now.")
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language='en-US')
    text=text.lower()
    print(f'You said: {text}')
    if text == "time":
        print("Time:", time)
    elif text == "temperature":
        print(f"The temperature in {city} is: {temperature}°C")
    elif text == "open mail":
        webbrowser.open("https://mail.google.com")
        print("Open mail...")
    else:
        print("no fuction assigned yet, try again")
