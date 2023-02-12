import discord
import random
from discord.ext import commands

from helpers import get_rps, play_rps, get_rpssl, play_rpssl

class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='choose', description='Chooses between multiple choices')
    async def choose(self, ctx, *choices: str):
        await ctx.send(random.choice(choices))

    @commands.command(name='flip', description='Flips a coin')
    async def flip(self, ctx):
        await ctx.send(random.choice(["Heads", "Tails"]))

    @commands.command(name='rps', description='Play Rock Paper Scissors')
    async def rps(self, ctx, *, choice: str=None):
        if choice is None:
            await ctx.send("```!rps {your-choice}\nRock (R), Paper (P), or Scissors (S).```")
            return
        try:
            choice = get_rps(choice)
        except Exception:
            await ctx.send('Invalid Choice')
        else:
            bot_choice = random.choice(["Rock", "Paper", "Scissors"])
            await ctx.send(f'You chose {choice}')
            await ctx.send(f'I choose {bot_choice}')
            await ctx.send(play_rps(choice, bot_choice))

    # Game inspired from this article
    # https://eduherminio.github.io/blog/rock-paper-scissors/
    @commands.command(name='rpssl', description='Play Rock Paper Scissors Spock Lizard')
    async def rpssl(self, ctx, *, choice: str=None):
        if choice is None:
            await ctx.send("```!rpsls {your-choice}\nRock (Ro), Paper (Pa), Scissors (Sc), Spock (Sp), and Lizard (Li).```")
            return
        try:
            choice = get_rpssl(choice)
        except Exception:
            await ctx.send('Invalid Choice')
        else:
            choices = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]
            await ctx.send(f'You chose {choices[choice]}')
            bot_choice = random.randint(0, 4)
            await ctx.send(f'I choose {choices[bot_choice]}')
            await ctx.send(play_rpssl(choice, bot_choice))

async def setup(bot):
    await bot.add_cog(Games(bot))