from discord.ext import commands
from core.helperFunctions import *

import random
import os

# TODO: Add fun commands

questions_path = os.path.join(uppath(__file__, 2), "core", "data", "questions.txt")

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["8ball", "eightball", "eight_ball", "magicball"])
    async def _8ball(self, ctx, *, question):
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Dont count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.']
        await ctx.send(embed = createStandardEmbed(ctx, f"The 8ball has spoken: {random.choice(responses)}", f"Your Question: {question}"))

    @commands.command(aliases=["topic", "q"])
    async def question(self, ctx):
        with open(questions_path, encoding='UTF-8') as f:
            content = f.readlines()
        await ctx.send(random.choice(content))
    
    @commands.command()
    async def rps(self, ctx, choice):
        CHOICES = ("rock", "paper", "scissors")
        while True:
            if choice not in CHOICES: 
                await ctx.send(embed = createStandardEmbed(ctx, "Please only type either rock, paper or scissors", "Error!"))
                continue
            cpu = random.choice(CHOICES)
            await ctx.send("I chose %s" % cpu)
            if choice != cpu: break
            await ctx.send(embed = createStandardEmbed(ctx, "Play again..", "We tied"))
        await ctx.send(embed = createStandardEmbed(ctx, "You %s!" % ("Win" if CHOICES[CHOICES.index(choice)-1] == cpu else "Lose"), "s%!" % ("Congrats" if CHOICES[CHOICES.index(choice)-1] == cpu else "Better luck next time"))


def setup(bot):
    bot.add_cog(FunCommands(bot))