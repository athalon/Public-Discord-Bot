from discord.ext import commands
from core.helperFunctions.helperFunctions import *

class TestCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def emtest(self, ctx):
        await ctx.send(createStandardEmbed(ctx, "Test Command", "Test"))

def setup(bot):
    bot.add_cog(TestCommands(bot))