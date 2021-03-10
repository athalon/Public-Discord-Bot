from discord.ext import commands
from core.helperFunctions import *

commands_tally = {
    
}

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    '''
    Successful and Invocation Handling
    '''
    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command is not None:
            if ctx.command.name in commands_tally:
                commands_tally[ctx.command.name] += 1
            else:
                commands_tally[ctx.command.name] = 1

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(ctx.command.name + " was invoked successfully")
    
    @commands.command()
    async def cmdtally(self, ctx):
        await ctx.send(commands_tally)


def setup(bot):
    bot.add_cog(CommandEvents(bot))