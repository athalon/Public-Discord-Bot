from discord.ext import commands
from core.helperFunctions.helperFunctions import *

class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test successful!")

def setup(bot):
    bot.add_cog(MiscCommands(bot))