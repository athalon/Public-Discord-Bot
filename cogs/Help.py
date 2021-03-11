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
        em = createHelpEmbed(ctx, self.bot, "8ball", "Ask a question to the magic 8ball!", "<question>", "None", "8ball, eightball, eight_ball, magicball")
        await ctx.send(embed = em)
    
    @help.command(name="question")
    async def question_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "question", "Asks you a random question", "", "None", "question, topic, q")
        await ctx.send(embed = em)
    
    @help.command(name="rps"):
    async def rps_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "rps", "Play rock-paper-scissors against the bot!", "<choice>", "None", "rps")
        await ctx.send(embed = em)
    
    @help.command(name="ping")
    async def ping_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "ping", "Displays the bots latency (ping)", "", "None", "ping")
        await ctx.send(embed = em)
    
    @help.command(name="random_number")
    async def rng_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "random_number", "Sends a random number", "<min> <max>", "None", "RNG, randint, randomnumber")
        await ctx.send(embed = em)
    
    @help.command(name="test")
    async def test_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "test", "General testing command", "", "None", "test")
        await ctx.send(embed = em)
    
    @help.command(name="ban")
    async def ban_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "ban", "Bans a member", "<member (id or @)> [reason]", "Ban Members", "ban")
        await ctx.send(embed = em)
    
    @help.command(name="kick")
    async def kick_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "kick", "Kicks a member", "<member (id or @)> [reason]", "Kick members", "kick")
        await ctx.send(embed = em)
    
    @help.command(name="mute")
    async def mute_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "mute", "Mutes a member", "<member (id or @)> [reason]", "Manage Roles", "mute")
        await ctx.send(embed = em)
    
    @help.command(name="unmute")
    async def unmute_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "unmute", "Unmutes a member", "<member (id or @)> [reason]", "Manage Roles", "unmute")
        await ctx.send(embed = em)
    
    @help.command(name="softban")
    async def softban_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "softban", "Softbans a member (ban, then unban)", "<member (id or @)> [reason]", "Ban Members", "softban")
        await ctx.send(embed = em)
    
    @help.command(name="unban")
    async def unban_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "unban", "Unbans a member", "<member (id or @)>", "Ban Members", "unban")
        await ctx.send(embed = em)

    @help.command(name="purge")
    async def purge_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "purge", "Mass-deletes messages", "<ammount>", "Manage Messages", "purge, clear, clean")
        await ctx.send(embed = em)

    @help.command(name="prefix")
    async def prefix_help(self, ctx):
        em = createHelpEmbed(ctx, self.bot, "prefix", "Either changes or views the prefix depending on if you specified a prefix", "[prefix]", "Administrator (when setting the prefix) | None (When viewing the prefix)", "prefix")
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(HelpCommands(bot))