import discord
from discord.ext import commands
import youtube_dl

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), ssl=False)


@bot.command()
async def play(ctx, url: str):
    await ctx.send('Playing...')
    ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    # Now we can play the downloaded file
    # assuming its mp3 format
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('song.mp3'))
    ctx.voice_client.play(source, after=lambda e: print(
        'Player error: %s' % e) if e else None)
    await ctx.send('Playing...')


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


TOKEN = 'YOUR TOKEN'

bot.run(TOKEN)
