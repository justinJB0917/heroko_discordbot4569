from distutils.command.clean import clean
from email import message, message_from_binary_file
from pyexpat.errors import messages
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


@client.event
async def on_message(message):
    
    if message.author.bot:
        return
    
    if client.user in message.mentions: 
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
        if content == '':
            content = first
        if translator.detect(content).lang == DSTLanguage:
            return
        if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
            remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage) 


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
