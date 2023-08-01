import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_by_date(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if date in item['dt_txt']:
                print(f"Temperature on {date}: {item['main']['temp']}°C")
                return
        print("No weather data available for the given date.")
    else:
        print("Failed to fetch data from the API.")

def get_wind_speed_by_date(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if date in item['dt_txt']:
                print(f"Wind Speed on {date}: {item['wind']['speed']} m/s")
                return
        print("No weather data available for the given date.")
    else:
        print("Failed to fetch data from the API.")

def get_pressure_by_date(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if date in item['dt_txt']:
                print(f"Pressure on {date}: {item['main']['pressure']} hPa")
                return
        print("No weather data available for the given date.")
    else:
        print("Failed to fetch data from the API.")

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        option = int(input("Enter your choice: "))

        if option == 1:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            get_weather_by_date(date)
        elif option == 2:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            get_wind_speed_by_date(date)
        elif option == 3:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            get_pressure_by_date(date)
        elif option == 0:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
