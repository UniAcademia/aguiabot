import constantes
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_permission
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="purge", description="Limpa N mensagens do chat.", guild_ids=[constantes.guild_id],
                       default_permission=False, permissions={
            constantes.guild_id: [
                create_permission(constantes.aguia_role_id, SlashCommandPermissionType.ROLE, True)
            ]
        })
    async def purge(self, ctx: SlashContext, qtde: int = 1):
        if qtde > 100:
            qtde = 100
        else:
            if qtde < 1:
                qtde = 1

        await ctx.send(f'Apagando {qtde} mensagens...', hidden=False, delete_after=1)
        primeira = True
        async for mensagem in ctx.channel.history(limit=qtde+1):
            try:
                if not primeira:
                    await mensagem.delete()
                else:
                    primeira = False
            finally:
                pass


def setup(bot):
    bot.add_cog(Purge(bot))
