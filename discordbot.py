from distutils.command.clean import clean
from email import message, message_from_binary_file
from pyexpat.errors import messages
from telnetlib import STATUS
import discord
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()


@client.event
async def on_ready():
    print('成功登入 登入身份：', client.user)
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
        await message.delete()

        await message.channel.send(tmp[1])
        print(client.user, '發送了', tmp[1],)

    if message.content == 'GG人':
        await message.delete()
        await message.channel.send("<你的訊息已被撤回>")
        print(client.user, '撤回了一則訊息', '內容：','(GG人)')

    if message.content == '機器人':
        await message.delete()
        await message.channel.send("<你的訊息已被撤回>")
        print(client.user, '撤回了一則訊息', '內容：','(機器人)')
    if message.content == '這裡的觀眾都是機器人嗎':
        await message.delete()
        await message.channel.send("<你已遭到 管理員Relaxing234的永久禁言>")
        print(client.user, '撤回了一則訊息', '內容：','(這裡的觀眾都是機器人嗎)')

    

client.run(TOKEN)
