import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True
_TOKEN = os.environ['TOKEN']
_WORK_CHANNEL = os.environ['work_channel']
_START_CHANNEL = os.environ['start_channel']
_TARGET_ID = os.environ['Target_ID']

@bot.event
async def on_ready():
    print('Bot is ready.')
    channel = bot.get_channel(_START_CHANNEL)
    await channel.send("開始工作")
@bot.event
async def on_message(message):
    channel = bot.get_channel(_WORK_CHANNEL)
    print(message.content)
    if message.author.id == _TARGET_ID:
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
      
bot.run(_TOKEN)
