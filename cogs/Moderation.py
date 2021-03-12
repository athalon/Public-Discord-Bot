import discord
from discord.ext import commands
from core.helperFunctions import *


# Checks if there is a muted role on the server and creates one if there isn't
async def mute(ctx, user, reason):
    role = discord.utils.get(ctx.guild.roles, name="Muted") # retrieves muted role returns none if there isn't 
    if not role: # checks if there is muted role
        muted = await ctx.guild.create_role(name="Muted", reason="Autocreate mute role")
        for channel in ctx.guild.channels: # removes permission to view and send in the channels 
            await channel.set_permissions(muted, send_messages=False)
        await user.add_roles(muted) # adds newly created muted role
        await ctx.send(embed=createStandardEmbed(ctx, f"{str(user)} has been muted for {reason}", "Muted!"))
        await user.send(embed=createStandardEmbed(ctx, f"You have been muted in {ctx.guild.name} for {reason}", "Muted!"))
    else:
        await user.add_roles(role) # adds already existing muted role
        await ctx.send(embed=createStandardEmbed(ctx, f"{str(user)} has been muted for {reason}", "Muted!"))
        await user.send(embed=createStandardEmbed(ctx, f"You have been muted in {ctx.guild.name} for {reason}", "Muted!"))

class Moderation(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user, reason="Reason not specified"):
        user = getMember(self.bot, user)
        await ctx.message.delete()
        await ctx.guild.ban(user, f"By {ctx.author} for {reason}")
        await ctx.send(embed=createStandardEmbed(ctx, f"{str(user)} has been banned for {reason}", "Banned!"))
        await user.send(embed=createStandardEmbed(ctx, f"You have been banned from {ctx.guild.name} for {reason}", "Banned!"))

    @commands.command()
    async def softban(self, ctx, user, reason="Reason not specified"): # Ban and instant unban
        user = getMember(self.bot, user)
        await ctx.message.delete()
        await ctx.guild.ban(user, f"Softbanned by {ctx.author} for {reason}") 
        await ctx.guild.unban(user, "Softban complete")
        await ctx.send(embed=createStandardEmbed(ctx, f"Softbanned {str(user)} for {reason}", "Softbanned!"))
        await user.send(embed=createStandardEmbed(ctx, f"You have been softbanned from {ctx.guild.name} for {reason}", "Softbanned!"))
    
    @commands.command()
    async def mute(self, ctx, user, reason="Reason not specified"):
        user = getMember(self.bot, user)
        await ctx.message.delete()
        await mute(ctx, user, reason) # uses the mute function
    
    @commands.command()
    async def kick(self, ctx, user, reason="Reason not specified"):
        user = getMember(self.bot, user)
        await ctx.message.delete()
        await ctx.guild.kick(user, f"By {ctx.author} for {reason}")
        await ctx.send(embed=createStandardEmbed(ctx, f"Kicked {str(user)} for {reason}", "Kicked!"))
        await user.send(embed=createStandardEmbed(ctx, f"You have been kiced from {ctx.guild.name} for {reason}", "Kicked!"))

    @commands.command(aliases=["clear", "clean"])
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1) # also deletes your own message
        await ctx.send(embed=createStandardEmbed(ctx, f"Bulk deleted `{limit}` messages", "Purged!"))
    
    @commands.command()
    async def unmute(self, ctx, user):
        user = getMember(self.bot, user)
        await ctx.message.delete()
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted")) # removes muted role
        await ctx.send(embed=createStandardEmbed(ctx, f"{user.mention} has been unmuted", "Unmuted!"))

          
def setup(bot):
    bot.add_cog(Moderation(bot))