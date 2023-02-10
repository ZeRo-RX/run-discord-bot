import discord
from discord.ext.commands import Bot, has_permissions

client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.members = True

TOKEN = 'your bot token'
ping_bot = Bot(intents = intents, command_prefix= "!")
                            
@ping_bot.command()
async def  on_ready(self):
        print("ready")

ping_bot.run(TOKEN)

