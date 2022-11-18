from discord.ext.commands import has_permissions
from discord.member import Member
from discord.ext import commands

class Expulsar(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_roles=True, kick_members=True)
    async def expulsar(self, ctx, member: Member):
        await ctx.guild.kick(member)


def setup(bot):
    bot.add_cog(Expulsar(bot))
