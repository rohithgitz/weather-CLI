import requests

def get_weather_data(city):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    data = response.json()
    return data

def get_temperature_by_date(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['main']['pressure']
    return None

def main():
    city = input("Enter the city name: ")
    data = get_weather_data(city)

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature_by_date(data, date)
            if temperature is not None:
                print(f"The temperature on {date} is {temperature} Kelvin.")
            else:
                print("Data not found for the given date.")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed} m/s.")
            else:
                print("Data not found for the given date.")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_by_date(data, date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure} hPa.")
            else:
                print("Data not found for the given date.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
