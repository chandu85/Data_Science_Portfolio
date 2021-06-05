# File: Yalamanchili_DSC510_Week10.py
# Name: Chandramouli Yalamanchili
# Date: 08/10/2019
# Course: DSC510-T302 - Introduction to programming (2197-1)
# Assignment: Final Project
# Desc: This program retrieves data from open weather API based on city name and zip code provided by user.
# Usage: Needed to register and acquire a working API key. User has to provide valid input to retrieve weather data.
#        US country is assumed for zip codes.

# Imports
import requests
import datetime

# API key used to invoke open weather map API services
# Replace - in with true value (reach out to Chandu for true value) for valid API key
api_key = "eb6d-d44723a8fd2f5-cbecf5fcfa-76"
reqUrl = "http://api.openweathermap.org/data/2.5/weather?APPID={}&units=imperial&"


# Methods
def retrieveWeatherByCity(city):
    """Prepare the request to invoke API using city name."""
    req = (reqUrl + "q={}").format(api_key, city)
    response = requests.get(req)
    return response


def retrieveWeatherByZip(zipCode):
    """Prepare the request to invoke API using zip code."""
    req = (reqUrl + "zip={},us").format(api_key, zipCode)
    response = requests.get(req)
    return response


def parseWeather(jsonMsg):
    """Prepare the response back to user based on data returned from open weather API service."""
    print("\n{:=<40}".format(""))
    print("{}".format("Weather details for {}, {}").format(jsonMsg["name"], jsonMsg["sys"]["country"]).center(40))
    print("{:=<40}".format(""))
    print("Current Conditions:")
    print(" {:18}:  {}°F".format("Temperature", jsonMsg["main"]["temp"]))
    print(" {:18}:  {}".format("Condition", jsonMsg["weather"][0]["description"]))
    if len(jsonMsg["weather"]) > 1:
        for cond in jsonMsg["weather"][1:]:
            if "description" in cond:
                print(" {:18}:  {}".format(" ", cond["description"]))
    if "pressure" in jsonMsg["main"]:
        print(" {:18}:  {} hPa".format("Pressure", jsonMsg["main"]["pressure"]))
    if "humidity" in jsonMsg["main"]:
        print(" {:18}:  {} %".format("Humidity", jsonMsg["main"]["humidity"]))
    if ("wind" in jsonMsg) & ("speed" in jsonMsg["wind"]) & ("deg" in jsonMsg["wind"]):
        print(" {:18}:  {} m/s, {}°".format("Wind", jsonMsg["wind"]["speed"], jsonMsg["wind"]["deg"]))
    print("\nForecast for whole day:")
    print(" {:18}:  {}°F".format("Minimum Temp", jsonMsg["main"]["temp_min"]))
    print(" {:18}:  {}°F".format("Maximum Temp", jsonMsg["main"]["temp_max"]))
    if ("sys" in jsonMsg) & ("sunrise" in jsonMsg["sys"]) & ("sunset" in jsonMsg["sys"]):
        print(" {:18}:  {} UTC".format("Sunrise", datetime.datetime.utcfromtimestamp(jsonMsg["sys"]["sunrise"],).ctime()))
        print(" {:18}:  {} UTC".format("Sunset", datetime.datetime.utcfromtimestamp(jsonMsg["sys"]["sunset"],).ctime()))
    print("{:=<40}".format(""))

def main():
    """This is the mainline function"""

    print("!!!Welcome to the weather application!!!")

    while True:
        location = input("\nPlease enter zip code (with in USA) or city name: ")

        response = None

        try:
            if location.isnumeric():
                response = retrieveWeatherByZip(location)
            else:
                response = retrieveWeatherByCity(location)
        except Exception as e:
            print("Not able to retrieve weather information for '{}'; error - {}".format(location, e))

        if (response is None):
            pass
        elif response.status_code != 200:
            print("Not able to retrieve weather information for '{}'; error - {}".format(location,
                                                                                         response.json()["message"]))
        else:
            try:
                parseWeather(response.json())
            except Exception as e:
                print("\nError in printing the details; error - {} not found".format(e))

        cont_flag = input("\nWould you like to pull weather data for some other location "
                          "(enter y to continue)? ")
        if cont_flag.lower() != "y":
            break

    print("\n!!!Thank you for using the weather application!!!")


if __name__ == '__main__':
    main()