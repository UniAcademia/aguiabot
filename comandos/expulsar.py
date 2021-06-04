from discord.ext.commands import has_permissions, Context
from discord.ext import commands
from utils import utils


class Expulsar(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members=True)
    async def expulsar(self, ctx: Context, mencao, *motivo):
        await ctx.message.delete()

        # region Obtém objeto do usuário mencionado
        id_usuario = utils.somente_numeros(mencao)
        if not id_usuario:
            return
        id_usuario = int(id_usuario)
        usuario = await self.bot.fetch_user(id_usuario)
        # endregion

        # region Validações

        try:
            if usuario.permissions_in(ctx.message.channel).kick_members:
                return
        finally:
            # O usuário não está no servidor
            pass

        motivo = ' '.join(motivo)
        if usuario is None or not motivo:
            return
        # endregion

    @expulsar.error
    async def expulsar_error(self, ctx: Context):
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Expulsar(bot))