import os
import random
import re
import discord
import typing
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_role, has_permissions

from helpers import find_user, get_rps, play_rps, get_rpssl, play_rpssl
import messages as ms

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

# PREP

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user.name} is connected to {guild.name}, at ID: {guild.id}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(ms.welcome_message.format(name=member.name))

# COMMANDS

@bot.command(name='av', description='Returns the avatar of the specified user')
async def av(ctx, *, user: str=None):
    if user is None:
        await ctx.send(ctx.author.display_avatar)
        return
    try:
        user = find_user(ctx.author, [u for u in ctx.guild.members], user)
    except Exception:
        await ctx.send('Member not found')
    else:
        await ctx.send(user.display_avatar)

# UTILITIES

@bot.command(name='choose', description='Chooses between multiple choices')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


@bot.command(name='flip', description='Flips a coin')
async def flip(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))


@bot.command(description='Shows when a member joined')
async def joined(ctx, member=None):
    if member is None:
        await ctx.send(f'{ctx.author.display_name} joined {ctx.guild.name} on {discord.utils.format_dt(ctx.author.joined_at)}')
    try:
        member = find_user(ctx.author, [u for u in ctx.guild.members], member)
    except Exception:
        await ctx.send('Member not found')
    else:
        await ctx.send(f'{member.display_name} joined {ctx.guild.name} on {discord.utils.format_dt(member.joined_at)}')

# GAMES

@bot.command(name='rps', description='Play Rock Paper Scissors')
async def rps(ctx, *, choice: str=None):
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
        await ctx.send(f'I chose {bot_choice}')
        await ctx.send(play_rps(choice, bot_choice))


# Game inspired from this article
# https://eduherminio.github.io/blog/rock-paper-scissors/
@bot.command(name='rpssl', description='Play Rock Paper Scissors Spock Lizard')
async def rpsls(ctx, *, choice: str=None):
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
        await ctx.send(f'I chose {choices[bot_choice]}')
        await ctx.send(play_rpssl(choice, bot_choice))

# PRIVILEDGED COMMANDS

@bot.command(name='purge', description='Deletes bulk messages')
@commands.has_role('The High Table')
async def delete_messages(ctx, *, count: int=10):
    if not 0 < count <= 100:
        await ctx.send("```!purge {number-of-messages}\nDeletes a 100 messages maximum.```")
    else:
        await ctx.channel.purge(limit=count)


@bot.command(name='kick', description='Deletes bulk messages')
@commands.has_role('The High Table')
async def kick(ctx, member: discord.Member, reason: str=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.display_name} has been kicked" + (reason) * f"for {reason}")

# ERRORS

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You are not authorised to execute this.', delete_after=5.0)


bot.run(TOKEN)