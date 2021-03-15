from discord.ext import commands
from core.helperFunctions import *
from pyowm.commons import exceptions as pywom_exceptions
from pyowm.owm import OWM
from os import getenv

owm = OWM(getenv('PYOWM_API_KEY'))
weather_manager = owm.weather_manager()

class WeatherCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def weather(self, ctx, location):
        try:
            weather = weather_manager.weather_at_place(location).weather
            temp_fahrenheit = weather.temperature('fahrenheit')
            temp_min_celcius = (int(temp_fahrenheit['temp_min'])-32)*5/9
            temp_max_celcius = (int(temp_fahrenheit['temp_max'])-32)*5/9
            weather_status = weather.detailed_status
            wind = weather.wind()
            msg = f"""It is currently {weather_status} in {location}
            The minumum temperature is {temp_fahrenheit['temp_min']}°F or {temp_min_celcius}°C
            The maximum temperature is {temp_fahrenheit['temp_max']}°F or {temp_max_celcius}°C
            The wind speed is {wind['speed']}m/s"""
            await ctx.send(embed=createStandardEmbed(ctx, msg, "Showing weather data for " + location))
        except pywom_exceptions.NotFoundError:
            await ctx.send(embed=createStandardEmbed(ctx, f"No weather data for the place {location} could be found. Please check your spelling", "Error!"))

def setup(bot):
    bot.add_cog(WeatherCommands(bot))