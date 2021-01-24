# bot.py
# encoding: utf-8
import os
import re
import random
import time
import discord
from dotenv import load_dotenv
import dice_lib

load_dotenv()
TOKEN = '<token>' #os.getenv()
class Ratio:
    value=10
    send=False
    servers=[]

client = discord.Client()
heresyQuotes = dice_lib.read_all_lines('./resources/quotes-heresy.txt')
diceReact = dice_lib.read_all_lines('./resources/quotes-dice.txt')
ratio=Ratio()

print(dice_lib.load_matches())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    option=random.choice(range(100))
    print(f'{client.user} {message.channel.type} Got message!, {option} > {message.content}')

    if message.author == client.user:
        return

    if f'{message.channel.type}' == 'private':
        if message.content.startswith('set ratio '):
            ratio.value=int(message.content.split(' ')[2])
            await message.channel.send(f'ratio {ratio.value}')
        elif message.content.startswith('get ratio'):
            await message.channel.send(f'ratio {ratio.value}')
        elif message.content.startswith('get inquisition'):
            await message.channel.send('\n'.join(heresyQuotes))
        elif message.content.startswith('add '):
            dice_lib.add_command(message.content)

        elif message.content.startswith('get '):
            await message.channel.send('\n'.join(dice_lib.get_command(message.content)))
        return

    #regex="(hereti[ck][a]?|heres[ye]|kac[ií][rř]|rouh[áa][ncč][ií]|herez[ií]|rouha[t]|ponny|magic|magie|demon|Gurnnink|REMD|[@][&!](753944326823739413|622701434713931776|320280460879986688)|dabel|devil)"
    isHeresy = re.search(dice_lib.load_matches(), message.content, re.IGNORECASE)
    if option >= ratio.value:
        return
    if isHeresy and ratio.send:
        response = random.choice(heresyQuotes)
        await message.reply(response)

    if re.search("(Papež Dice I|Dice Roll Boom)") and ratio.send:
        response = random.choice(diceReact)
        await message.reply(response)


client.run(TOKEN)
