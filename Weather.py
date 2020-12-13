import requests, json
def start():
    api_key = "dd38163a86988950d160a7ffd8f3874d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name: ")
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url) 
    x = response.json() 
 
    y = x["main"] 
    current_temperature_kelvin = y["temp"]
    current_temperature_celsius = current_temperature_kelvin - 273.15
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"] 
    weather_description = z[0]["description"] 
    print(" Temperature = " +
                    str(current_temperature_celsius.__round__(2)) +(" Degree Celsius")  +
        "\n Atmospheric Pressure = " +
                    str(current_pressure) + " hPa" +
        "\n Humidity = " +
                    str(current_humidiy) + "%" +
        "\n Description = " +
                    str(weather_description.capitalize()))
    def restartornot():
        restartornot = input("Do you want to restart?")
        if restartornot == "Y":
            start()
        elif restartornot == "y":
            start()
        elif restartornot == "n":
            exit()
        elif restartornot == "N":
            exit()
        else:
            print("Invalid Input")
            restartornot()
    restartornot()

start()