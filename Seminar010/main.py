import pyowm

owm = pyowm.OWM('dbf1c716cecbf43263218e4e0505968c', language='ru')
print(type(owm))
while True:
    place = input('В каком городе/стране?: ')


    observation = owm.weather_at_place(place)
    w = observation.get_weather()


    temp = w.get_temperature('celsius')['temp']

    print('В городе ' + place + " сейчас " + w.get_detailed_status())
    print('Температура сейчас в районе ' + str(temp))

print(type(observation)) # выдает следующее:
                         # <class 'pyowm.weatherapi25.observation.Observation'>

print(type(w)) # выдает следующее:
               # <class 'pyowm.weatherapi25.weather.Weather'>