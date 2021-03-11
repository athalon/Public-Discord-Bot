import discord
from replit import db
import os

def createStandardEmbed(ctx, description, title):
    embed = discord.Embed(
        description = description,
        color = 0xd303fc,
        timestamp = ctx.message.created_at
    )
    embed.set_author(name=title, icon_url='https://cdn.discordapp.com/attachments/790920201217769513/818984229722652722/Robot_Head.jpg')
    embed.set_footer(text=ctx.bot.user.name)
    return embed

def getPrefix(client, ctx):
    prefix = str(db[str(ctx.guild.id)])
    return prefix

def writeToDb(key, value):
    db[str(key)] = str(value)

def deleteDbEntry(key):
    del db[str(key)]

def createHelpEmbed(ctx, client, name, description, params, req_perms, aliases):
    embed = createStandardEmbed(ctx, description, name + " help")
    prefix = getPrefix(client, ctx)
    embed.add_field(name="Syntax", value=prefix+name+" "+params, inline=False)
    embed.add_field(name="Required Permissions", value=req_perms, inline=False)
    embed.add_field(name="Aliases", value=aliases, inline=False)
    
    return embed

uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])