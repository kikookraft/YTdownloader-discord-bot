import interactions # pip install -U discord-py-interactions
from interactions.ext.files import command_edit
import asyncio # lib already installed
import youtube_dl # pip install youtube_dl
# pip install -U interactions-files

with open('key', 'r') as f:
    bot_key = f.read()

bot = interactions.Client(token=bot_key, default_scope=704297527557619772)

# shutdown command
@bot.command(
    name = "shutdown",
    description = "Shuts down the bot")
async def shutdown(ctx: interactions.CommandContext):
    await ctx.send("Shutting down...")
    await asyncio.sleep(1)
    await bot._logout()
    exit()

# ping command
@bot.command(
    name="ping",
    description="Pings the bot")
async def ping(ctx: interactions.CommandContext):
    await ctx.send("Pong!")

# restart command
@bot.command(
    name="restart",
    description="Restarts the bot")
async def restart(ctx: interactions.CommandContext):
    await ctx.send("Restarting...")
    import sys
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")
    import os
    os.execv(sys.executable, ['python'] + sys.argv)
    

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
    
    try:
        video_info = youtube_dl.YoutubeDL().extract_info(url = link,download=False)
        filename = f"download/{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        await ctx.send(f"Downloading _{video_info['title']}_...\n_This may take a while..._")
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        file = interactions.File(filename)
        await command_edit(content=f"{ctx.user.mention} Downloaded _{video_info['title']}_!",files=file, ctx=ctx)
        
    except youtube_dl.utils.DownloadError:
        await ctx.send(f"Cant download audio from this link!")
        
    


    

bot.start()
