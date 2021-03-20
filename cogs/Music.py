from discord.ext import commands
from core.helperFunctions import *
import youtube_dl

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def music_test(self, ctx):
        await ctx.send("It works!")

def setup(bot):
    bot.add_cog(MusicCommands(bot))