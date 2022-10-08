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
    
    if client.user in message.mentions: # @判定
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
    if message.content == '哈囉':
        await message.channel.send('閉嘴啦吵死了')  
    if message.content == 'hi':
        await message.channel.send('hi屁')
    if message.content == '好哦':
        await message.channel.send('閉嘴啦誰說好了')   
    if message.content == '掰掰':
        await message.channel.send('再見你可以滾去吃屎了')
    if message.content == '拜拜':
        await message.channel.send('快滾去拜拜 字都不會打啊？ 欠電')
    if message.content == '私訊':
        await message.channel.send('我不想回你欸')  
    if message.content == '笨':
        await message.channel.send('你比較笨') 
    if message.content == '醜':
        await message.channel.send('你比較醜')    
    if message.content == '可愛':
        await message.channel.send('你很醜')
    if message.content == '我很正':
        await message.channel.send('你很醜')
    if message.content == 'XD':
        await message.channel.send('笑屁')
    if message.content == 'www':
        await message.channel.send('笑屁')
    if message.content == '2333':
        await message.channel.send('笑屁')    
    if message.content == '嘿':
        await message.channel.send('嘿個屁')    
    if message.content == '加油':
        await message.channel.send('95還無鉛')
    if message.content == '早安':
        await message.channel.send('美好的一天 從看見你開始 變得不美好')
    if message.content == '午安':
        await message.channel.send('午安 要來點屎給你當午餐嗎？')
    if message.content == '晚安':
        await message.channel.send('給我滾去睡覺 現在立刻 少給我廢話')
    if message.content == '對':
        await message.channel.send('對屁') 
    if message.content == '愛你':
        await message.channel.send('請你滾')
    if message.content == '喜歡你':
        await message.channel.send('請你現在立刻滾')
    if message.content == '啾咪':
        await message.channel.send('滾遠一點')
    if message.content == '吵':
        await message.channel.send('你才吵 可憐')
    if message.content == '可憐':
        await message.channel.send('你才可憐 孤兒')  
    if message.content == '喔':
        await message.channel.send('喔是喔 關我屁事喔')
    if message.content == '累':
        await message.channel.send('累就去睡 在這邊GGYY')
    if message.content == '笑死':
        await message.channel.send('笑屁 有你的臉好笑嗎')    
    if message.content == 'Ok':
        await message.channel.send('誰說OK了')    
        

client.run(TOKEN)
