from discord.ext import commands
from core.helperFunctions import *
import random

class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test successful!")
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(embed = createStandardEmbed(ctx, f"Client latency: {round(self.bot.latency * 1000)}ms", "ping_pong:Pong!"))

    @commands.command(aliases=["RNG", "randint", "randomnumber"])
    async def random_number(self, ctx, min: int, max: int):
        await ctx.send(embed = createStandardEmbed(ctx, f"Number: {str(random.randint(min, max))}", "Random Number Generator"))

def setup(bot):
    bot.add_cog(MiscCommands(bot))