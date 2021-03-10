from discord.ext import commands
from discord.ext.commands import bot
from core.helperFunctions.helperFunctions import *
import os

default_prefix = '.'
prefix_path = os.path.abspath(__file__ + "/../../core/data/prefixes.json")

class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild): # When the client is invited to a server, create a json entry with the default prefix
        with open(prefix_path, 'r') as f:
            prefixes = json.load(f)
        
        prefixes[str(guild.id)] = default_prefix

        with open(prefix_path, 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild): # When the client is kicked/banned from a guild, remove the json entry
        with open(prefix_path, 'r') as f:
            prefixes = json.load()
        
        prefixes.pop(str(guild.id))

        with open(prefix_path, 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.command()
    async def prefix(self, ctx, prefix):
        if prefix:
            with open(prefix_path, 'r') as f:
                prefixes = json.load(f)
            
            prefixes[str(ctx.guild.id)] = prefix
            
            with open(prefix_path) as f:
                json.dump(prefixes, f, indent=4)
        else:
            with open(prefix_path, 'r') as f:
                prefixes = json.load(f)
            
            guild_prefix = prefixes[str(ctx.guild.id)]
            await ctx.send(embed = createStandardEmbed(ctx, f"The current prefix for this server is `{guild_prefix}`!\n*You can change this by typing `{guild_prefix}prefix [new_prefix]`", "Guild Prefix"))

            with open(prefix_path, 'w') as f:
                json.dump(prefixes, f, indent=4)


def setup(bot):
    bot.add_cog(Prefix(bot))