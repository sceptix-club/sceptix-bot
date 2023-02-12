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

    


if __name__ == "__main__":
    asyncio.run(main())

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.errors.CheckFailure):
#         await ctx.send('You are not authorised to execute this.', delete_after=5.0)
