from discord.ext import commands
from core.helperFunctions import *

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send(embed = createStandardEmbed(ctx, "Help Command Placeholder", "Help Command"))

def setup(bot):
    bot.add_cog(HelpCommands(bot))