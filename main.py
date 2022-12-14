import interactions # pip install -U discord-py-interactions
import asyncio # lib already installed
from pytube import YouTube # pip install pytube3

with open('key', 'r') as f:
    bot_key = f.read()

bot = interactions.Client(token=bot_key, default_scope=704297527557619772)


@bot.command(
    name = "shutdown",
    description = "Shuts down the bot")
async def shutdown(ctx: interactions.CommandContext):
    await ctx.send("Shutting down...")
    await asyncio.sleep(1)
    await bot._logout()
    exit()


@bot.command()
@interactions.option()
async def purge(ctx: interactions.CommandContext, quantity: int):
    """Purges a number of messages"""
    await ctx.send(f"Purging {quantity} messages...")
    await asyncio.sleep(2)
    await ctx.channel.purge(quantity+1)



# download audio of the yt link on parameter
@bot.command()
@interactions.option()
async def download(ctx: interactions.CommandContext, link: str):
    """Download audio from youtube link
    CAN TAKE A WHILE TO DOWNLOAD"""
    await ctx.defer()
    
    # download the video
    # video_info = youtube_dl.YoutubeDL().extract_info(url = link,download=True)
    # filename = f"download/{video_info['title']}.mp3"
    # options={
    #     'format':'bestaudio/good',
    #     'keepvideo':False,
    #     'outtmpl':filename,
    # }
    # with youtube_dl.YoutubeDL(options) as ydl:
    #     ydl.download([video_info['webpage_url']])
    try:
        yt = YouTube(link).streams.filter(only_audio=True, file_extension="mp3").first()
        yt.download(output_path=f"download\\{yt.default_filename}.mp3")
        await ctx.send(f"Downloaded {yt.title} !")
    except AttributeError as e:
        await ctx.send(f"Cant download audio from this link!\n{e}")
        
    


    

bot.start()
