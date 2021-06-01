from discord.ext.commands import has_permissions, Context
from discord.ext import commands


class Purge(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members=True)
    async def purge(self, ctx: Context, qtde: int = 1):
        # region Filtra qtde
        if qtde > 100:
            qtde = 100
        else:
            if qtde < 1:
                qtde = 1
        # endregion

        # region Apaga as mensagens
        await ctx.message.delete()

        async for mensagem in ctx.channel.history(limit=qtde):
            try:
                await mensagem.delete()
            finally:
                break
        # endregion

    @purge.error
    async def purge_error(self, ctx: Context):
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Purge(bot))
