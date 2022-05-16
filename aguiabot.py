import os
import models
from discord_slash import SlashCommand
from discord.ext import commands
from dotenv import load_dotenv

eventos = ['on_ready']
comandos = ['purge', 'avisar']


def carregar_eventos(bot):
    for evento in eventos:
        try:
            bot.load_extension(f'eventos.{evento}')
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Erro ao carregar evento {evento}\n{exc}')


def carregar_comandos(bot):
    for comando in comandos:
        try:
            bot.load_extension(f'comandos.{comando}')
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Erro ao carregar comando {comando}\n{exc}')


def iniciar_bot():
    models.criar_tabelas()  # carrega as tabelas do banco de dados
    load_dotenv()  # carrega as variáveis de ambiente (arquivo .env)
    token = os.getenv('DISCORD_TOKEN')
    bot = commands.Bot(command_prefix='!')

    _ = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)  # Não apagar essa linha
    carregar_eventos(bot)
    carregar_comandos(bot)
    bot.run(token)


if __name__ == '__main__':
    iniciar_bot()
