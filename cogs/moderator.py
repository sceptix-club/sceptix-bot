import discord
from discord.ext import commands
from discord.ext.commands import has_role, has_permissions

class Moderator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='purge', description='Deletes bulk messages')
    @commands.has_role('The High Table')
    async def delete_messages(self, ctx, *, count: int=10, msg_type: str=None):
        if not 0 < count <= 100:
            await ctx.send("```!purge {number-of-messages}\nDeletes a 100 messages maximum.```")
            return
        
        if msg_type is None:
            await ctx.channel.purge(limit=count, check=lambda m: not m.pinned)
            return

        if "bot" in msg_type.lower():
            await ctx.channel.purge(limit=count, check=lambda m: m.author.bot)
            return


    @commands.command(name='kick', description='Deletes bulk messages')
    @commands.has_role('The High Table')
    async def kick(self, ctx, member: discord.Member, reason: str=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.display_name} has been kicked" + (reason) * f"for {reason}")


    @commands.command(name='roleadd', description='Adds a specified role to all the human members of the server')
    @commands.has_role('The High Table')
    async def roleadd(self, ctx, role: discord.Role):
        for u in ctx.guild.members:
            if not u.bot:
                await u.add_roles(ctx.guild.get_role(role.id))
        await ctx.send(f'{role.name} added')


    @commands.command(name='roleremove', description='Removes a specified role to all the human members of the server')
    @commands.has_role('The High Table')
    async def roleremove(self, ctx, role: discord.Role):
        for u in ctx.guild.members:
            if not u.bot:
                await u.remove_roles(ctx.guild.get_role(role.id))
        await ctx.send(f'{role.name} removed')


async def setup(bot):
    await bot.add_cog(Moderator(bot))