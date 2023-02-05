import os
import discord
from discord.ext import commands

UNVERIFIED_ID = os.getenv('UNVERIFIED_ID')
GUILD = os.getenv('GUILD')

class Listener(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game('with your heart'))
        guild = discord.utils.get(self.bot.guilds, name=GUILD)
        print(f'{self.bot.user.name} is connected to {guild.name}. ID: {guild.id}.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(ms.dm_message.format(name=member.name))
        guild = discord.utils.get(self.bot.guilds, name=GUILD)
        await member.add_roles(guild.get_role(UNVERIFIED_ID))


async def setup(bot):
    await bot.add_cog(Listener(bot))