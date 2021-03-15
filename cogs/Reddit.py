from discord.ext import commands
from core.helperFunctions import *
from random import randint
from aiohttp import ClientSession

prev_seed = None

class RedditCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def meme(self, ctx):
        async with ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                img_seed = randint(0, 25)
								if img_seed == prev_seed: img_seed = randint(0, 25)
                title = res['data']['children'] [img_seed]['title']

                img_url = res['data']['children'] [img_seed]['data']['url']

                em = createStandardEmbed(ctx, "", title)
                em.set_image(url=img_url)
                await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(RedditCommands(bot))