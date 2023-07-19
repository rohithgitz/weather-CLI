# Weather Forecast CLI

## Description

Weather Forecast CLI is a Python command-line interface (CLI) application that fetches hourly weather forecasts for a specified location using the OpenWeatherMap API. The user can interact with the program and select from various options to obtain weather information, including temperature, wind speed, and pressure, for specific dates.

## Requirements

- Python 3.x
- requests library

## Installation

1. Clone the repository: git clone https://github.com/rohithgitz/weather-CLI.git
2.  Navigate to the project directory: cd weather-CLI
3. Install the required dependencies: pip install requests

## Usage

1. Run the program:
python3 weather_cli.py


2. Enter the city name when prompted.

3. Choose from the following options:
- 1: Get weather
- 2: Get Wind Speed
- 3: Get Pressure
- 0: Exit

4. If you choose option 1, enter the date in the format (YYYY-MM-DD HH:MM:SS) to get the temperature for that date.
If you choose option 2, enter the date to get the wind speed.
If you choose option 3, enter the date to get the pressure.

5. The program will display the corresponding weather information for the chosen date.

## Example

Enter the city name: Munich

Options:

Get weather
Get Wind Speed
Get Pressure
Exit
Enter your choice: 1
Enter the date (YYYY-MM-DD HH:MM:SS): 2023-07-20 12:00:00
The temperature on 2023-07-20 12:00:00 is 295.12 Kelvin.

Enter your choice: 2
Enter the date (YYYY-MM-DD HH:MM:SS): 2023-07-20 12:00:00
The wind speed on 2023-07-20 12:00:00 is 3.62 m/s.

Enter your choice: 0
Exiting the program.
