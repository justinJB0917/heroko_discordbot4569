from email import message_from_binary_file
import discord
import googletrans
import os
from pprint import pprint

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
      
    if len(tmp) ==1:
        await messagechannel.send("語法錯誤")
        else:
        await message.channel.send(tmp[1])
        
    if message.content.startwith('更改狀態'):
        tmp = message.content.split(" ",2)

        if len(tmp) == 1:
            await message.channel.send("你要改什麼你要說啊") 
        else:
            game = discord.Game(tmp[1])       
            await client.change_presence(status=discord.Status.idle, activity=game)
        

client.run(TOKEN)
