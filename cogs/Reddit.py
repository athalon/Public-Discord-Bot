from discord.ext import commands
from core.helperFunctions import *
from random import randint
from aiohttp import ClientSession

class RedditCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def meme(self, ctx):
        async with ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                em = createStandardEmbed(ctx, "", "Random Meme")
                em.set_image(url=res['data']['children'] [randint(0, 35)]['data']['url'])
                await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(RedditCommands(bot))