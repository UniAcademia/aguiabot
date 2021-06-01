from discord.ext.commands import has_permissions, Context
from discord.ext import commands
from utils import utils
from models import Avisos
from servicos.dm_service import DmService


class Avisar(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members=True)
    async def avisar(self, ctx: Context, mencao, *motivo):
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

        # region Envia DMs
        _ = await DmService().enviar_dm(usuario, f'Você recebeu um aviso de {ctx.author.mention}: "{motivo}"')
        _ = await DmService().enviar_dm(ctx.author, f'Você enviou um aviso para {usuario.mention}: "{motivo}"')
        # endregion

        # region Persistencia
        _ = Avisos.create(
            id_usuario=id_usuario,
            id_emissor=ctx.author.id,
            descricao=motivo)
        # endregion

    @avisar.error
    async def avisar_error(self, ctx: Context):
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Avisar(bot))
