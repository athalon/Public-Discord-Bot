import discord
from discord.ext import commands
from core.helperFunctions import *

# TODO: Add comand aliases
# TODO: Make the bot delete the message that invoked the command
# TODO: Rewrite the moderation system to work with the new discord.py version

# This prevents staff members from being punished 
class Sinner(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets a member object
        permission = argument.guild_permissions.manage_messages # can change into any permission
        if not permission: # checks if user has the permission
            return argument # returns user object
        else:
            raise commands.BadArgument("You cannot punish other staff members") # tells user that target is a staff member

# Checks if you have a muted role
class Redeemed(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets member object
        muted = discord.utils.get(ctx.guild.roles, name="Muted") # gets role object
        if muted in argument.roles: # checks if user has muted role
            return argument # returns member object if there is muted role
        else:
            raise commands.BadArgument("The user was not muted.") # self-explainatory
            
# Checks if there is a muted role on the server and creates one if there isn't
async def mute(ctx, user, reason):
    role = discord.utils.get(ctx.guild.roles, name="Muted") # retrieves muted role returns none if there isn't 
    if not role: # checks if there is muted role
        try: # creates muted role 
            muted = await ctx.guild.create_role(name="Muted", reason="Autocreate mute role")
            for channel in ctx.guild.channels: # removes permission to view and send in the channels 
                await channel.set_permissions(muted, send_messages=False)
        except discord.Forbidden:
            return await ctx.send("I have no permissions to make a muted role") # self-explainatory
        await user.add_roles(muted) # adds newly created muted role
        await ctx.send(embed = createStandardEmbed(ctx, f"{str(user)} has been muted for {reason}", "Muted!"))
        await user.send(embed = createStandardEmbed(ctx, f"You have been muted in {ctx.guild.name} for {reason}", "Muted!"))
    else:
        await user.add_roles(role) # adds already existing muted role
        await ctx.send(embed = createStandardEmbed(ctx, f"{str(user)} has been muted for {reason}", "Muted!"))
        await user.send(embed = createStandardEmbed(ctx, f"You have been muted in {ctx.guild.name} for {reason}", "Muted!"))


class Moderation(commands.Cog):
    """Commands used to moderate your guild"""
    
    def __init__(self, bot):
        self.bot = bot
    
    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
            
    @commands.command(aliases=["banish"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: Sinner=None, reason=None):
        """Casts users out of heaven."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to ban user
            await ctx.guild.ban(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified")
            await ctx.send(createStandardEmbed(ctx, f"{str(user)} has been banned for {reason}" or f"{str(user)}", "Banned!"))
            await user.send(createStandardEmbed(ctx, f"You have been banned from {ctx.guild.name} for {reason}" or f"You have been banned from {ctx.guild.name}", "Banned!"))
        except discord.Forbidden:
            return await ctx.send("Are you trying to ban someone higher than the bot")

    @commands.command()
    async def softban(self, ctx, user: Sinner=None, reason=None):
        """Temporarily restricts access to heaven."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to soft-ban user
            await ctx.guild.ban(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified") 
            await ctx.guild.unban(user, "Temporarily Banned")
            await ctx.send(createStandardEmbed(ctx, f"Softbanned {str(user)} for {reason}" or f"Softbanned {str(user)}", "Softbanned!"))
            await user.send(createStandardEmbed(ctx, f"You have been softbanned from {ctx.guild.name} for {reason}" or f"You have been softbanned from {ctx.guild.name}", "Softbanned!"))
        except discord.Forbidden:
            return await ctx.send("Are you trying to soft-ban someone higher than the bot?")
    
    @commands.command()
    async def mute(self, ctx, user: Sinner, reason=None):
        """Gives them hell."""
        await mute(ctx, user, reason or "None specified") # uses the mute function
    
    @commands.command()
    async def kick(self, ctx, user: Sinner=None, reason=None):
        if not user: # checks if there is a user 
            return await ctx.send("You must specify a user")
        
        try: # tries to kick user
            await ctx.guild.kick(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified")
            await ctx.send(createStandardEmbed(ctx, f"Kicked {str(user)} for {reason}" or f"Kicked {str(user)}", "Kicked!"))
            await user.send(createStandardEmbed(ctx, f"You have been kiced from {ctx.guild.name} for {reason}" or f"You have been kicked from {ctx.guild.name}", "Kicked!"))
        except discord.Forbidden:
            return await ctx.send("Are you trying to kick someone higher than the bot?")

    @commands.command()
    async def purge(self, ctx, limit: int):
        """Bulk deletes messages"""
        
        await ctx.purge(limit=limit + 1) # also deletes your own message
        await ctx.send(createStandardEmbed(ctx, f"Bulk deleted `{limit}` messages", "Purged!"))
    
    @commands.command()
    async def unmute(self, ctx, user: Redeemed):
        """Unmutes a muted user"""
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted")) # removes muted role
        await ctx.send(createStandardEmbed(ctx, f"{user.mention} has been unmuted", "Unmuted!"))

          
def setup(bot):
    bot.add_cog(Moderation(bot))