"""To run this console app, you will need the following APIs:
-> openweathermap
-> ExchangeRate-API
Both APIs require a login to be made to retrieve a key, but are both free for under a certain number of requests.
Type in the name of the API and follow the signup information."""


import requests
from pprint import pprint as pp
from api_keys import api_key_weather, api_key_currency



print("Welcome to Johnson's Holidays! Here you will find some useful information about your trip for the next 5 days.")
print("Find out the weather for the next 5 days in your location. We'll give you some hints about what to pack!")
print("We can also tell you what the currency is, what the current exchange rate is, and tell you how much you might want to take.")

#Where are you going?
holiday_location_question = input("Where are you going on your holiday? ")
current_location_question = input("Where are you currently? ")


"""
Weather Forecast!
In this section, I have used openweathermap api to find the weather forecast for the input location. 
It gives you the forecast for 5 days in 3 hour intervals. 
I have collected the temperatures to work out the average temperature over the next 5 days.
"""


weather_url = f"https://api.openweathermap.org/data/2.5/forecast?q={holiday_location_question}&APPID={api_key_weather}&units=metric"
weather_data = requests.get(weather_url)
#print(temp)

"""This is how I got the temperature"""

temp = weather_data.json()

all_temps = 0.0
length = 0

for d in temp["list"]:
    all_temps = float(all_temps) + float(d["main"]["temp"])
for d in temp["list"]:
    length = length + 1

# print(length)

average_temp = all_temps / length


"""I then collected the different types of weather in the forecast and worked out the most common, therefore most likely to happen in the next 5 days"""

weather_type = str()

for d in temp["list"]:
    weather_type = weather_type + ", " + str(d["weather"][0]["main"])

weather_list = weather_type.split(", ")
weather_list2 = weather_list[1:]

# print(weather_list2)

weather_list_set = set(weather_list2)

# print(weather_list_set)


thunderstorm = 0  # 200 - 232
drizzle = 0  # 300 -
rain = 0  # 500
snow = 0  # 600
poor_visability = 0  # 700
mist = 0  # 701
fog = 0  # 741
clear = 0  # ==800
clouds = 0  # 801

for d in temp["list"]:
    if d["weather"][0]["id"] >= 801:
        clouds = clouds + 1
    elif d["weather"][0]["id"] == 800:
        clear = clear + 1
    elif d["weather"][0]["id"] == 741:
        fog = fog + 1
    elif d["weather"][0]["id"] == 701:
        mist = mist + 1
    elif d["weather"][0]["id"] >= 700:
        poor_visability = poor_visability + 1
    elif d["weather"][0]["id"] >= 600:
        snow = snow + 1
    elif d["weather"][0]["id"] >= 500:
        rain = rain + 1
    elif d["weather"][0]["id"] >= 300:
        drizzle = drizzle + 1
    elif d["weather"][0]["id"] >= 200:
        thunderstorm = thunderstorm + 1
    else:
        print("weather error")

weather_frequency = f"thunderstorm: {thunderstorm}, drizzle: {drizzle}, rain: {rain}, snow: {snow}, poor_visability: {poor_visability}, mist: {mist}, fog: {fog}, clear: {clear}, clouds: {clouds}"

# print(weather_frequency)

weather_frequency_list = weather_frequency.split(", ")

# print(weather_frequency_list)

weather_frequency_dict = {}
for weather in weather_frequency_list:
    i = weather.split(": ")
    weather_frequency_dict[i[0]] = i[1]
# print(weather_frequency_dict)


main_weather = max(weather_frequency_dict, key=weather_frequency_dict.get).title()
# print(main_weather)

"""Printing the weather information together"""

print(f"The average temperature in {holiday_location_question} for the next 5 days is: {round(average_temp)}°C")

for i in weather_list_set:
    if i == main_weather:
        print(f"The weather will mostly be {i}.")
    else:
        print(f"There might be some {i} weather.")

if main_weather == "Thunderstorm" or "Rain" or "Drizzle":
    print("Pack your waterproofs! The weather is looking wet.")
elif main_weather == "Snow":
    print("Pack your thermals!")
elif main_weather == "Clear":
    print("It's going to be sunny! Pack some suncream!")


if average_temp >= 20:
    print("It's going to be warm! Pack shorts and a t-shirts!")
elif average_temp > 10:
    print("It might be a bit chilly, pack some jumpers.")
elif average_temp > 0:
    print("It's going to be cold, you'll need a coat.")
elif average_temp < 0:
    print("Pack your thermals! It's freezing!")

"""I then used ExchangeRate-API to collect the information about the exchange rate.
You will need to import the function in the file currency_codes.py to work out the exchange rate.
This file will be in the branch in GitHub."""

from currency_codes import iso_code_finder

current_location = iso_code_finder(current_location_question)
holiday_location = iso_code_finder(holiday_location_question)

currency_url = f"https://v6.exchangerate-api.com/v6/{api_key_currency}/pair/{current_location}/{holiday_location}"
currency = requests.get(currency_url)
data = currency.json()
#print(data)
exchange_rate = data["conversion_rate"]
print(f"1 {current_location} is currently equal to {exchange_rate} {holiday_location}")

current50 = 50 * float(exchange_rate)
current100 = 100 * float(exchange_rate)

print(f"50 {current_location} is equal to {current50} {holiday_location}.")
print(f"100 {current_location} is equal to {current100} {holiday_location}.")

amount = input("How much money do you want to take? (e.g. 45) ")
amount_exchanged = float(amount) * float(exchange_rate)
print(f"{amount} {current_location} is {amount_exchanged} {holiday_location}")

"""Text file with key information about your trip."""

with open("holiday.txt", "w+") as text_file:
    holiday = f"You are going to {holiday_location_question} \nYou are travelling from {current_location_question}."
    weather = f"\nThe weather is likely to be {main_weather} and around {round(average_temp)}°C."
    currency_convert = f"\n1 {current_location} is currently equal to {exchange_rate} {holiday_location}."
    text_file.write(holiday)
    text_file.write(weather)
    text_file.write(currency_convert)