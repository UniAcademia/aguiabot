import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions
from datetime import datetime

def send_temp_message(ctx, msg, tempo):
    """
    :param ctx: Contexto
    :param msg: Mensagem que vai ser enviada
    :param tempo: O tempo em segundos até a mensagem ser apagada
    """
    if isinstance(msg, discord.Embed):
        temp_msg = await ctx.send(embed=msg)
    else:
        temp_msg = await ctx.send(msg)
    await asyncio.sleep(tempo)
    await msg.delete()

def iniciar_bot():
    # carrega as variáveis de ambiente (as variáveis que não podem ser públicas, como o token do Bot)
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print(f'{bot.user} se conectou ao Discord!')

    @bot.command()
    @has_permissions(kick_members=True)
    async def purge(ctx, qtde=1):
        """
        Apaga as n últimas mensagens do chat
        :param ctx: Contexto
        :param qtde: Quantidade de mensagens a serem apagadas. Valor padrão: 1
        """

        # apaga a mensagem do comando
        await ctx.message.delete()

        if qtde > 100:
            qtde = 100
        else:
            if qtde < 1:
                qtde = 1

        async for mensagem in ctx.history(limit=qtde):
            try:
                await mensagem.delete()
            finally:
                break

        horario = datetime.now().strftime('%H:%M')
        embed = discord.Embed(title=f'Um administrador limpou {qtde} mensagens do chat', color=0x00afff)
        embed.set_author(name=f'🧹 O chat foi limpo!')
        embed.set_footer(text=f'Hoje às {horario}')
        send_temp_message(ctx, embed, 30)

    @purge.error
    async def purge_error(ctx):
        await ctx.message.delete()

    bot.run(token)


if __name__ == '__main__':
    iniciar_bot()
