from __future__ import unicode_literals
from discord.ext import commands
from core.helperFunctions import *
import youtube_dl
import os

#TODO: Fix the music downloading or just give up and try to do it by the shitty youtube tutorials

output_path = os.path.dirname(__file__)
output_path = uppath(output_path, 2)
output_path = os.path.join(output_path, 'core', 'data')

ydl_opts = {
    'format': 'bestaudio/best',
    'download_archive': 'downloaded_songs.txt',
    'outtmpl': str(output_path) + '/%(title)s.%(ext)s',
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