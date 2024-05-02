import requests

def get_weather_data(city="rajkot"):

    api_key = "2606f769271b8d545fe3458b2b72ed9f"

    final_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

    try:
        result = requests.get(final_url)
        result.raise_for_status()  

        if result.status_code == 200:
            data = result.json()

            ctemp = data["main"]["temp"] - 273.15 
            ktemp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print("\nMaster : Weather Data of " + data["name"])
            print("\nTemperature (Celsius):", ctemp)
            print("Temperature (Kelvin):", ktemp)
            print("Humidity:", humidity)
            print("Wind Speed:", wind_speed)

        else:
            print("\nOOPS Master : Failed to retrieve weather data. Status code:", result.status_code)

    except requests.exceptions.RequestException as e:
        print("\nOOPs Master : Network is not available OR City Name Is Invalid , Please Check The Things.")
