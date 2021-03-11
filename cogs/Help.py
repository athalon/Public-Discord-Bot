from discord.ext import commands
from discord.utils import get
from core.helperFunctions import *

# TODO: Create help commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        em = createStandardEmbed(ctx, f"Use {getPrefix(self.bot, ctx)}help <command> for more info on a specific command.")
        em.add_field(name=":game_die: Fun", value="8ball, question, rps", inline=False)
        em.add_field(name=":question: Misc", value="ping, random_number, test, prefix", inline=False)
        em.add_field(name=":hammer: Moderation", value="kick, ban, unban, mute, unmute, purge, softban", inline=False)
        await ctx.send(embed = em)
    
    @help.command(name="8ball")
    async def _8ball_help(self, ctx):
        em = createStandardEmbed(ctx, "Ask a question to the magic 8ball!", "8ball help")
        em.add_field(name="**Syntax**", value=f"{getPrefix(self.bot, ctx)}8ball <question>", inline=False)
        em.add_field(name="**Required Permissions**", value="None", inline=False)
        em.add_field(name="**Aliases**", value="8ball, eightball, eight_ball, magicball")
        await ctx.send(embed = em)
        em = createHelpEmbed(ctx, self.bot, "8ball", "Ask a question to the magic 8ball!", "<question>", "None", "8ball, eightball, eight_ball, magicball")
        await ctx.send(embed = em)

    
    @help.command(name="question")
    async def question_help(self, ctx):
        em = createStandardEmbed(ctx, "Asks you a random question!", "question help")
        em.add_field(name="**Syntax**", value=f"{getPrefix(self.bot, ctx)}question", inline=False)
        em.add_field(name="**Required Permissions**", value="None", inline=False)
        em.add_field(name="**Aliases**", value="topic, q")

def setup(bot):
    bot.add_cog(HelpCommands(bot))