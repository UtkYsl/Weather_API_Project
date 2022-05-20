import datetime as dt
import requests

baseurl = "http://api.openweathermap.org/data/2.5/weather?"
api_key = open('api_key','r').read()
city = (input("Hangi şehrin hava durumunu öğrenmek istersiniz?:"))

def kelvin_to_celcius_fahrenheit(kelvin):
    celcius = kelvin - 273.15
    return celcius

url = baseurl + "appid=" + api_key + "&q=" + city
responce = requests.get(url).json()

temp_kelvin = responce['main']['temp']
temp_celcius = kelvin_to_celcius_fahrenheit(temp_kelvin)
feels_like_kelvin = responce['main']['feels_like']
feels_like_celcius = kelvin_to_celcius_fahrenheit(feels_like_kelvin)
humidity = responce['main']['humidity']
description = responce['weather'][0]['description']
wind_speed = responce['wind']['speed']
sunrise_time = dt.datetime.utcfromtimestamp(responce['sys']['sunrise'] + responce['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(responce['sys']['sunset'] + responce['timezone'])

print(f"{city}'de Sıcaklık: {temp_celcius:.2f}°C")
print(f"{city}'de Hissedilen sıcaklık: {feels_like_celcius:.2f}°C")
print(f"{city}'de nem: {humidity}%")
print(f"{city}'de Rüzgar Hızı: {wind_speed}m/s")
print(f"{city}'de genel hava durumu: {description}")
print(f"{city}'de Güneş Doğumu: {sunrise_time}")
print(f"{city}'de Güneş Batımı: {sunset_time}")





