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
            temp_celcius = weather.temperature('celcius')
            weather_status = weather.detailed_status
            wind = weather.wind()
            msg = f"""It is currently {weather_status} in {location}
            The minumum temperature is {temp_fahrenheit['temp_min']}°F or {temp_celcius['temp_min']}°C
            The maximum temperature is {temp_fahrenheit['temp_max']}°F or {temp_celcius['temp_max']}°C
            The wind speed is {wind['speed']}m/s"""
            await ctx.send(embed=createStandardEmbed(ctx, msg, "Showing weather data for " + location))
        except pywom_exceptions.NotFoundError:
            await ctx.send(embed=createStandardEmbed(ctx, f"No weather data for the place {location} could be found. Please check your spelling", "Error!"))

def setup(bot):
    bot.add_cog(WeatherCommands(bot))