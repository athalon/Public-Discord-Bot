# TODO: Implement into the bot
# For more code snippets and advice, visit https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html

from pyowm.commons import exceptions as pyowm_exeptions
from pyowm.owm import OWM

owm = OWM('a0cacf2e476dbcd05060cc464db3c528') # Please use the enviroment variable PYOWM_API_KEY for this in the final version. You can access this using os.getenv('PYOWM_API_KEY')
weather_manager = owm.weather_manager()

place = input("City name: ").capitalize()

try:
    weather = weather_manager.weather_at_place(place).weather

    temp_dict_fahrenheit = weather.temperature('fahrenheit')
    temp_min_celcius = (int(temp_dict_fahrenheit['temp_min'])-32)*5/9
    temp_max_celcius = (int(temp_dict_fahrenheit['temp_max'])-32)*5/9
    weather_status = weather.detailed_status
    wind_dict = weather.wind()
    print(f"""The weather in {place} is {weather_status}
    The minimum temperature is {temp_dict_fahrenheit['temp_min']}°F or {temp_min_celcius}°C
    The maximum temperature is {temp_dict_fahrenheit['temp_max']}°F or {temp_max_celcius}°C
    The wind speed is {wind_dict['speed']}
    """)
except pyowm_exeptions.NotFoundError:
    print("Error!\nCouldn't obtain weather data from that location")