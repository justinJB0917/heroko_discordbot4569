from distutils.command.clean import clean
from email import message, message_from_binary_file
from pydoc import cli
from pyexpat.errors import messages
from telnetlib import STATUS
import discord
import os
from pprint import pprint
import time

TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()


@client.event
async def on_ready():
    print('成功登入')
    game = discord.Game('vscode 我也想擁有智慧')
    await client.change_presence(status=discord.Status.idle, activity=game)




@client.event

async def on_message(message):
    
    if message.author == client.user:
        return
    #-------------(防止讀取自己的訊息進入回圈）----------------------------------------------------------#
    if message.content.startswith('說'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("要讓我說話嗎 你想要我說什麼？")
      else:
        await message.delete()
        await message.channel.send(tmp[1])
        print(client.user, '發送了', tmp[1])
    #-----------------------------------------------------------------------------------------------#
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
    #-----------------------------------------------------------------------------------------------#
    if message.content == '奇怪的叡':
        await message.channel.send("觸發彩蛋 送你一張照片:)  https://ibb.co/rsHSw7F")
        print(client.user, '觸發了1號彩蛋')
    if message.content == '中二丁丁':
        await message.channel.send("觸發彩蛋 送你一張照片:)  https://ibb.co/GPsnS4N")
        print(client.user, '觸發了4號彩蛋')
    if message.content == '顏利窘':
        await message.channel.send("觸發彩蛋 送你一張照片:)  https://ibb.co/1fH2p9C")
        print(client.user, '觸發了14號彩蛋')
    if message.content == '綠藻頭':
        await message.channel.send("觸發彩蛋 送你一張照片:)  https://ibb.co/9wH4NJC")
        print(client.user, '觸發了25號彩蛋')
    if message.content == '偏笨':
        await message.channel.send("觸發彩蛋 送你一張照片:)  https://ibb.co/YkHqS7J 弄你我可能會被踢出去:D")
        print(client.user, '觸發了20號彩蛋')
    if message.content == 'Aidan Lu':
        await message.channel.send("觸發彩蛋 送你一張照片:)  https://ibb.co/Cm0vZKW")
        print(client.user, '觸發了10號彩蛋')
    if message.content == '禿頭怪人':
        await message.channel.send("觸發彩蛋 送你一張照片:)  https://ibb.co/k8T7sBb")
        print(client.user, '觸發了26號彩蛋')
    #-----------------------------------------------------------------------------------------------#





@client.event
async def on_member_join(member):
    print(F'{member}join!')
    channel = client.get_channel(1028857081593340004)
    await channel.send(F'{member}join!')

@client.event
async def on_member_remove(member):
    print(F'{member}leave!')
    channel = client.get_channel(1028858150457184260)
    await channel.send(F'{member}leave!')

    
client.run(TOKEN)
