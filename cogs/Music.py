from discord.ext import commands
from core.helperFunctions import *
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def music_test(self, ctx, link):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        await ctx.send("Audio downloaded!")

def setup(bot):
    bot.add_cog(MusicCommands(bot))