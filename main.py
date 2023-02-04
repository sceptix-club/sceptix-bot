import os
import random
import re
import discord
import typing
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands

from helpers import find_user
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
async def av(ctx, *, user=None):
    if user is None:
        await ctx.send(ctx.author.display_avatar)
    try:
        user = find_user(ctx.author, [u for u in ctx.guild.members], user)
    except Exception:
        await ctx.send('Member not found')
    else:
        await ctx.send(user.display_avatar)


@bot.command(name='choose', description='Chooses between multiple choices')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


@bot.command(name='flip', description='Flips a coin')
async def flip(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))


# @bot.command(name='repeat',description='Repeats a message numtiple times')
# async def repeat(ctx, *, times: int=0, content=None):
#     if not 1 <= times <= 10:
#         await ctx.send("```!repeat {number-of-times} {content}\nRepeat 1 to 10 times only.```")
#         return
    
#     if content is None:
#         content = f'{ctx.author.name} is cool!'

#     for i in range(times):
#         await ctx.send(content)


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


# PRIVILEDGED COMMANDS

@bot.command(name='purge', description='Deletes bulk messages')
@commands.has_role('Council')
async def delete_messages(ctx, *, count: int=10):
    if not 0 < count <= 100:
        await ctx.send("```!purge {number-of-messages}\nDeletes a 100 messages maximum.```")
    else:
        await ctx.channel.purge(limit=count)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You are not a Council Member.')



bot.run(TOKEN)