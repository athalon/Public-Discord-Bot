from discord.ext import commands
from core.helperFunctions import *

# TODO: Add fun commands

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def placeholder_fun_command(self, ctx):
        await ctx.send(embed = createStandardEmbed(ctx, "This is a placeholder command for the Fun Commands Cog", "Placeholder Fun Command"))

def setup(bot):
    bot.add_cog(FunCommands(bot))