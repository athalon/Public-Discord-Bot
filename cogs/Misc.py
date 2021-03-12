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
        await ctx.send(.send(embed=createStandardEmbed(ctx, f"Client latency: {round(self.bot.latency * 1000)}ms", "ping_pong:Pong!"))

    @commands.command(aliases=["RNG", "randint", "randomnumber"])
    async def random_number(self, ctx, min: int, max: int):
        await ctx.send(.send(embed=createStandardEmbed(ctx, f"Number: {str(random.randint(min, max))}", "Random Number Generator"))

    @commands.command(aliases=["servercount", "server"])
    async def servers(self, ctx):
        await ctx.send(.send(embed=createStandardEmbed(ctx, f"I am currently on {len(self.bot.guilds)} servers :smile:", "In how many servers am I?"))

def setup(bot):
    bot.add_cog(MiscCommands(bot))