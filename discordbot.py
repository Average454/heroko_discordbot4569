import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True

@bot.event
async def on_ready():
    print('Bot is ready.')
    channel = bot.get_channel(803625496675483662)
    await channel.send("開始工作")
@bot.event
async def on_message(message):
    channel = bot.get_channel(1081939437094711316)
    print(message.content)
    if message.author.id == 694519530981949482:
        if message.attachments:
            print("傳了一張圖片")
            # 逐一處理圖片並傳送到頻道中
            for attachment in message.attachments:
                await channel.send(f"{message.author.mention} 傳送了以下圖片：")
                await channel.send(attachment.url)
                if  message.content != "":
                    await channel.send(f"{message.author.mention} 傳送了以下訊息：")
                    await channel.send(message.content)
           
        
        else:
            await message.channel.send(f"{message.author.mention} 傳送了以下訊息：")
            await channel.send(message.content)
      
bot.run('MTA4MTUxMTE2Njc1ODYyMTIyNQ.Gm1tDS.0Fi2MMlF1wSkUPtUzim7zT2B2fnU8IZTAmxtoo')
