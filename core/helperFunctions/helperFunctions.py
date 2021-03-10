import discord
import json
import os

prefix_path = os.path.abspath(__file__ + "/../data/prefixes.json")

def createStandardEmbed(ctx, description, title):
    embed = discord.Embed(
        description = description,
        color = 0xd303fc,
        timestamp = ctx.message.created_at
    )
    embed.set_author(name=title, icon_url='https://cdn.discordapp.com/attachments/790920201217769513/818984229722652722/Robot_Head.jpg')
    embed.set_footer(text=ctx.bot.user.name)
    return embed

def getPrefix(client, message):
    with open('./core/data/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]