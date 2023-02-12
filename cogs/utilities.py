import os
import discord
from discord.ext import commands
from discord.ext.commands import has_role, has_permissions

import messages as ms
from helpers import find_user

UNVERIFIED_ID = int(os.getenv('UNVERIFIED_ID'))
VERIFIED_ID = int(os.getenv('VERIFIED_ID'))
WELCOME_ID = int(os.getenv('WELCOME_ID'))

class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='av', description='Returns the avatar of the specified user')
    async def av(self, ctx, *, user: str=None):
        if user is None:
            await ctx.send(ctx.author.display_avatar)
            return
        try:
            # Used instead of Guild.get_member_named() for better UX
            user = find_user(ctx.author, [u for u in ctx.guild.members], user)
        except Exception:
            await ctx.send('Member not found')
        else:
            await ctx.send(user.display_avatar)

    @commands.command(description='Shows when a member joined')
    async def joined(self, ctx, member=None):
        if member is None:
            await ctx.send(f'{ctx.author.display_name} joined {ctx.guild.name} on {discord.utils.format_dt(ctx.author.joined_at)}')
            return
        try:
            # Used instead of Guild.get_member_named() for better UX
            member = find_user(ctx.author, [u for u in ctx.guild.members], member)
        except Exception:
            await ctx.send('Member not found')
        else:
            await ctx.send(f'{member.display_name} joined {ctx.guild.name} on {discord.utils.format_dt(member.joined_at)}')

    @commands.command(description='Returns the ping of the bot')
    async def ping(self, ctx):
        pong = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! {pong}ms")

    @commands.command(name='announce', description='Announces a message as an embed')
    @commands.has_role('The High Table')
    async def announce(self, ctx, channel: discord.TextChannel, heading: str, content: str):
        embed = discord.Embed(title=heading, description=content, colour=0x48cae4)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await channel.send(content='@everyone', embed=embed)

    @commands.command(name='verify', description='Allows an unverified user access to the server')
    @commands.has_role('unverified')
    async def verify(self, ctx, *name):
        if ctx.channel != ctx.guild.get_channel(WELCOME_ID):
            return

        name = ' '.join(name).title()
        await ctx.author.edit(nick=name)
        await ctx.channel.purge(limit=100, check=lambda m: not m.pinned)
        await ctx.author.add_roles(ctx.guild.get_role(VERIFIED_ID))
        await ctx.author.remove_roles(ctx.guild.get_role(UNVERIFIED_ID))


async def setup(bot):
    await bot.add_cog(Utilities(bot))