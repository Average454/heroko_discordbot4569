import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True
TOKEN = os.environ['TOKEN']
work_channel = os.environ['work_channel']
start_channel os.environ['start_channel']
Target_ID = os.environ['Target_ID']

@bot.event
async def on_ready():
    print('Bot is ready.')
    channel = bot.get_channel(start_channel)
    await channel.send("開始工作")
@bot.event
async def on_message(message):
    channel = bot.get_channel(work_channel)
    print(message.content)
    if message.author.id == Target_ID:
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
      
bot.run(TOKEN)
