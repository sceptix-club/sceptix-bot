import os
import discord
from discord.ext import commands

import messages as ms
from helpers import find_user

GUILD = os.getenv('DISCORD_GUILD')
WELCOME_CHANNEL_ID = 1071774146998055033
UNVERIFIED_ID = 1071774242460405780
VERIFIED_ID = 1071778379499573350

class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
        await bot.change_presence(activity=discord.Game('with your heart'))
        guild = discord.utils.get(bot.guilds, name=GUILD)
        print(f'{bot.user.name} is connected to {guild.name}. ID: {guild.id}.')
    
    @commands.Cog.listener()
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(ms.dm_message.format(name=member.name))
        guild = discord.utils.get(bot.guilds, name=GUILD)
        await member.add_roles(guild.get_role(UNVERIFIED_ID))

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
        try:
            # Used instead of Guild.get_member_named() for better UX
            member = find_user(ctx.author, [u for u in ctx.guild.members], member)
        except Exception:
            await ctx.send('Member not found')
        else:
            await ctx.send(f'{member.display_name} joined {ctx.guild.name} on {discord.utils.format_dt(member.joined_at)}')


    @commands.command(name='announce', description='Announces a message as an embed')
    @commands.has_role('The High Table')
    async def announce(self, ctx, channel: discord.TextChannel, heading: str, content: str):
        embed = discord.Embed(title=heading, description=content, colour=0x48cae4)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await channel.send(content='@everyone', embed=embed)


    @commands.command(name='verify', description='Allows an unverified user access to the server')
    @commands.has_role('unverified')
    async def verify_me(self, ctx, *name):
        if ctx.channel != ctx.guild.get_channel(WELCOME_CHANNEL_ID):
            return

        name = ' '.join(name).title()
        await ctx.author.edit(nick=name)
        await ctx.author.add_roles(ctx.guild.get_role(VERIFIED_ID))
        await ctx.author.remove_roles(ctx.guild.get_role(UNVERIFIED_ID))
        await ctx.channel.purge(100, check=lambda m: not m.pinned)


async def setup(bot):
    await bot.add_cog(Utilities(bot))