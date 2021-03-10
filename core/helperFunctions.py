import discord
from replit import db

def createStandardEmbed(ctx, description, title):
    embed = discord.Embed(
        description = description,
        color = 0xd303fc,
        timestamp = ctx.message.created_at
    )
    embed.set_author(name=title, icon_url='https://cdn.discordapp.com/attachments/790920201217769513/818984229722652722/Robot_Head.jpg')
    embed.set_footer(text=ctx.bot.user.name)
    return embed

def getPrefix(ctx):
    prefix = str(db[str(ctx.guild.id)])

def writeToDb(key, value):
    db[str(key)] = str(value)

def deleteDbEntry(key):
    del db[str(key)]