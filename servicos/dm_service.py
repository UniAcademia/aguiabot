import discord


class DmService:
    @staticmethod
    async def enviar_dm(membro: discord.User, mensagem):
        try:
            canal = await membro.create_dm()
            await canal.send(mensagem)
            return True
        except Exception as e:
            return e
