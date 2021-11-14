import os
import discord
import random
from keep_alive import keep_alive

client = discord.Client()

pessoas = ["Youiti","Roberto","Matheus","Ricardo","Maikon","Henrique","Victor", "youit", "youti", "ricardo",  "roberto", "maik", "maikon", "matheus","renan","Renan","felipe","Felipe","henrique","menezes","Menezes","mim"]

leo = ["Leo", "Rato", "verme","leo","rato","LEO"]

palhaços = ["shaco","Shaco","Coringa", "coringa","joker"]

mulheres = ["Rafaella","rafaella","rafaela","Rafaela"]

respostas_iniciais = [
    "Ja comi",
    "ja vi a mae desse ai pelada",
    "Esse ai é um bosta",
    "sla, bora abrir uma adega no seu nome?",
    "Esse cara já me viu pelado e gostou",
    "Delicia demais",
    "Bumbum guloso",
    "Tem o pau maior que o meu",
    "a Rafaella me trocou por ele",
    "fiquei sabendo que já namorou com o Leo Couto",
    "esse ai só me afunda no lol"

]

respostas_convocaçao =[
    "Fala logo porra",
    "vou pegar a manteiguinha",
    "Sou eu, hahaha!",
    "Fala fio",
    "Vem dar um beijo no shacola",
    "to fazendo um churrasco calmae",
    "o Main Shaco tá on fio"
]

respostas_palhaço =[
    "chora pro shaco do pai",
    "nois é joker mesmo fodase",
    "HAHAHAHAHAHAHAHAHAHAHAHAHA"
]

respostas_jogos=[
    "jogo lixo",
    "só se for agora",
    "cszada?",
    "só faltava não",
    "não dá, to no plants"
]

jogos = ["LoL","lol","Lol","MIR4","Valorant","valorant","cs","Rail Roads"]

Lima = [
    "Lima",
    "lima"
]

respostas_mulheres =[
    "Já limpei a mesa com essa",
    "comi na pscina no ano novo",
    "https://www.youtube.com/watch?v=T_lvyOTg5hk"
]

@client.event
async def on_ready():
    print('O main Shaco esta online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('?'):
        await message.channel.send('Sua mãe não tava me mandando interrogação ontem')


    if message.content.startswith('dama'):
        await message.channel.send('minha amada esposa')

    if message.content.startswith('Dama'):
        await message.channel.send('gostosa')

    if any(word in msg for word in Lima):
        await message.channel.send('Corno perneta')
    
    if any(word in msg for word in mulheres):
        await message.channel.send(random.choice(respostas_mulheres))

    if any(word in msg for word in jogos):
        await message.channel.send(random.choice(respostas_jogos))

    if message.content.startswith('Quem esta ai?'):
        await message.channel.send('Sou eu!! hahahaha 🤡')

    if any(word in msg for word in pessoas):
        await message.channel.send(random.choice(respostas_iniciais))

    if any(word in msg for word in leo):
        await message.channel.send(random.choice(respostas_convocaçao))

    if any(word in msg for word in palhaços):
        await message.channel.send(random.choice(respostas_palhaço))

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)