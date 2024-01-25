#make a HTTP request to a web page using python
#import datetime to convert unix time to datetime format
import requests
import datetime
#enter the api key from the open weather website
APIKey = 'c6cda76bc282fb7d642bafbb8a4be70a'
#store the base url
BaseURL = 'http://api.openweathermap.org/data/2.5/weather'
#f strings help in concatenating variables together and overall better formatting of our python code
#store and print greetings
Greeting = 'Welcome to Weather tracker! which city would you like to view'
print(Greeting)
City = input('Enter a City name: ')
RequestURL = f'{BaseURL}?appid={APIKey}&q={City}'
Response = requests.get(RequestURL)

#if repose is 'ok' hen get the whole JSON weather data as a pythin dictionary
if Response.status_code == 200:
    Data = Response.json()
    weather = Data['weather'][0]['description']
    temperature = round(Data['main']['temp'] - 273.15,2)
    sunrise = datetime.datetime.utcfromtimestamp(Data['sys']['sunrise']+Data['timezone'])
    sunset = datetime.datetime.utcfromtimestamp(Data['sys']['sunset']+Data['timezone'])
    
    print("weather summary: ",weather)
    print("The temperature is",temperature,'celcius')
    print("the sunrise time is",sunrise)
    print("the sunset time is",sunset)
else:
    print("Hmm.....that is not right")

    