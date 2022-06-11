import discord
from discord.ext import commands

bot = commands.Bot("!")

#2)
@bot.event
async def on_ready():
    embed = discord.Embed(
        title="Novo Ticket",
        description="Para criar um novo ticket reaja com 📰 abaixo! Se sua reação não for removida automaticamente, remova-a e tente novamente. Estamos ansiosos para ajudá-lo"
    )
    channel = bot.get_channel()#ID do canal tickets
    await channel.send(embed=embed)

#3)
@bot.event
async def on_raw_reaction_add(reaction):
    if reaction.emoji=="📰":
        channel = bot.get_channel()#ID do canal tickets abertos
        await channel.send('user')

bot.run("TOKEN")