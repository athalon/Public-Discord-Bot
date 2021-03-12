"""
For a list of exceptions:
https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#exceptions
"""

from core.helperFunctions import *
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            desc = f"Missing required Argument: {error.param.name}"
        elif isinstance(error, commands.CommandNotFound):
            desc = f"The command named {ctx.comand} does not exist"
        elif isinstance(error, commands.DisabledCommand):
            desc = f"The command named {ctx.command} is disabled"
        elif isinstance(error, commands.CommandInvokeError):
            desc = f"Error raised while command invokation: {error.original}"
        elif isinstance(error, commands.CommandOnCooldown):
            desc = f"The command is on cooldown. You can use the command again in {error.retry_after}s"
        elif isinstance(error, commands.MemberNotFound):
            desc = f"The member {str(error.argument)} could not be found"
        elif isinstance(error, commands.MissingPermissions):
            desc = f"You are lacking these permissions to run the command: {', '.join(error.missing_perms)}"
        elif isinstance(error, commands.BotMissingPermissions):
            desc = f"I am lacking these permission to run the command: {', '.join(error.missing_perms)}"
        elif isinstance(error, commands.ExtensionNotFound):
            desc = f"The cog {error.name} was not found"

        await ctx.send(embed = createStandardEmbed(ctx, desc, "Error!"))


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))