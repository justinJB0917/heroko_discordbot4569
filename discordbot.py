from distutils.command.clean import clean
from email import message, message_from_binary_file
from pyexpat.errors import messages
from telnetlib import STATUS
import discord
import googletrans
import os
from pprint import pprint
import asyncio

TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()


@client.event
async def on_ready():
    print('成功登入')
    game = discord.Game('Twitch 並觀賞Namin的直播')
    await client.change_presence(status=discord.Status.idle, activity=game)




@client.event

async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content.startswith('說'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("要讓我說話嗎 你想要我說什麼？")
      else:
        await message.channel.send(tmp[1])


@client.event

async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content == '嗨':
        await message.channel.send('嗨智障')

    


        

client.run(TOKEN)
