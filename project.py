import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
from messages import help_message

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

extensions = ['cogs.games', 'cogs.utilities', 'cogs.moderator', 'cogs.listener',]

async def main():
    for ext in extensions:
        await bot.load_extension(ext)

    bot.remove_command("help")

    @bot.command(name='help')
    async def help_func(ctx):
        await ctx.send(help_message)

    await bot.start(TOKEN)

# HELPER FUNCTIONS DUPLICATED TO MEET CS50P REQUIREMENTS

def get_rps(choice: str) -> str:
    choice = choice.lower().strip()
    if choice.startswith('r'):
        return "Rock"
    if choice.startswith('p'):
        return "Paper"
    if choice.startswith('s'):
        return "Scissors"
    raise Exception('Invalid Choice')


def play_rps(my_choice: str, bot_choice: str) -> str:
    if my_choice == "Rock" and bot_choice == "Scissors":
        return "You Won!"
    if my_choice == "Paper" and bot_choice == "Rock":
        return "You Won!"
    if my_choice == "Scissors" and bot_choice == "Paper":
        return "You Won!"
    if my_choice == bot_choice:
        return "That's a tie!"
    return "You lost \U0001F641"


def get_rpssl(choice: str) -> int:
    choice = choice.lower().strip()
    if choice.startswith('r'): return 0
    if choice.startswith('p'): return 1
    if choice.startswith('sc'): return 2
    if choice.startswith('sp'): return 3
    if choice.startswith('l'): return 4
    raise Exception('Invalid Choice')

# MAIN PROGRAM

if __name__ == "__main__":
    asyncio.run(main())