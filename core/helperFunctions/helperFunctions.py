import discord

def createStandardEmbed(ctx, description, author):
    embed = discord.Embed(
        description = description,
        color = 0xd303fc,
        timestamp = ctx.message.created_at
    )
    embed.set_author(name=author, icon_url='https://cdn.discordapp.com/attachments/790920201217769513/818984229722652722/Robot_Head.jpg')
    embed.set_footer(text=ctx.bot.user.name)
    return embed