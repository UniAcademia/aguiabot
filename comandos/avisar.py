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
        # try:
        #     if usuario.permissions_in(ctx.message.channel).kick_members:
        #         return
        # finally:
        #     # O usuário não está no servidor
        #     pass

        motivo = ' '.join(motivo)
        if usuario is None or not motivo:
            return
        # endregion

        # region Persistencia
        _ = Avisos.create(
            id_usuario=id_usuario,
            id_emissor=ctx.author.id,
            descricao=motivo)
        # endregion

        # region Contador de Avisos

        selecionar_Avisos=Avisos.select().where(Avisos.id_usuario == id_usuario)
        qtde_Avisos=selecionar_Avisos.count()

        # endregion

        # region Envia DMs
        _ = await DmService().enviar_dm(usuario, f'Você recebeu um aviso de {ctx.author.mention}: "{motivo}"\n Você possui: {qtde_Avisos} Avisos.\n Caso Esteja Recebendo/Receba o 3º Aviso será Expulso')
        _ = await DmService().enviar_dm(ctx.author, f'Você enviou um aviso para {usuario.mention}: "{motivo}"\n O {usuario.mention} possui: {qtde_Avisos} Avisos.')
        # endregion

        # region Expular Caso com 3 Avisos
        if qtde_Avisos>=3:
            await DmService().enviar_dm(usuario,f"Você foi expulso do Servidor: {ctx.guild}. por ter Recebido seu 3º Aviso") # Aviso de Expulsão DM 
            await ctx.send(f"{usuario} foi Expulso por ter Recebido seu 3º Aviso.") # Aviso de Expulsão Servidor
            await DmService().enviar_dm(ctx.author,f"O Usuario {usuario.mention} foi Expulso com sucesso do Servidor: {ctx.guild}. por ter Recebido seu 3º Aviso") # Aviso de Expulsão DM Admin
            await ctx.guild.kick(usuario) # Expulsar o Usuario
        # endregion
        
    @avisar.error
    async def avisar_error(self, ctx: Context):
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Avisar(bot))
