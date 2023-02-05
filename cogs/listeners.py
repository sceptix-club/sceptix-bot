import os
import discord
from discord.ext import commands

UNVERIFIED_ID = os.getenv('UNVERIFIED_ID')

class Listeners(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await bot.change_presence(activity=discord.Game('with your heart'))
        print(f'{bot.user.name} is connected to {bot.guild.name}. ID: {bot.guild.id}.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(ms.dm_message.format(name=member.name))
        await member.add_roles(bot.guild.get_role(UNVERIFIED_ID))


async def setup(bot):
    await bot.add_cog(Listeners(bot))