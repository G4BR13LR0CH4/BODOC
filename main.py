import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from gtoken import retornatoken

comando = ["$turma entrar", "$turma sair", "$turma entrar", "$infos"]

client = discord.Client()

msg_id = None
msg_user = None

@client.event
async def on_ready():
    print('Rodando {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('fodase! turma add'):
        await message.channel.send('Esse comando permite que você adicione uma turma/cargo!')
    
    elif message.content.startswith('fodase! turma sair'):
        await message.channel.send('Esse comando permite que você  saia de uma turma/cargo que você está incluso!')
    
    elif message.content.startswith('fodase! turma entrar'):
        embed1 = discord.Embed(
                    title="Escolha a turma que deseja entrar!",
                    color=0x690FC3,
                    description="- IHC = 🐤\n"
                        "- Grafos  =  📘 \n"
                        "- LIP-Rodrigo  = 📙",)

        botmsg = await message.channel.send(embed=embed1)

        await botmsg.add_reaction("🐤")
        await botmsg.add_reaction("📘")
        await botmsg.add_reaction("📙")
        global msg_id
        msg_id = botmsg.id

    elif message.content.startswith('fodase! info'):
        await message.channel.send('O BODOC tem como objetivo reunir alunos das mesmas turmas ' +
        'facilitando assim a comunicação entre eles.')
        mensagem = "\nEsses são todos os comandos disponiveis:"
        for item in comando:
            if item == "$infos":
                mensagem += "\n" + item
            else:
                mensagem += "\n" + item + " nome_da_turma"
        await message.channel.send(mensagem)
        
 
    global msg_user
    msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🐤" and msg.id == msg_id and user.id != client.user.id:
        await user.add_roles(get(reaction.message.guild.roles, name="IHC"))

    elif reaction.emoji == "📘" and msg.id == msg_id and user.id != client.user.id:
        await user.add_roles(get(reaction.message.guild.roles, name="Grafos"))

    elif reaction.emoji == "📙" and msg.id == msg.id and user.id != client.user.id:
         await user.add_roles(get(reaction.message.guild.roles, name="LIP-Rodrigo"))


@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🐤" and msg.id == msg_id and user.id != client.user.id:
        await user.remove_roles(get(reaction.message.guild.roles, name="IHC"))

    elif reaction.emoji == "📘" and msg.id == msg_id and user.id != client.user.id:
        await user.remove_roles(get(reaction.message.guild.roles, name="Grafos"))

    elif reaction.emoji == "📙" and msg.id == msg.id and user.id != client.user.id:
         await user.remove_roles(get(reaction.message.guild.roles, name="LIP-Rodrigo"))

client.run(retornatoken())