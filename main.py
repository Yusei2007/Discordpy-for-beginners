import discord
from discord.ext import commands
import os 
import keep_alive
keep_alive.keep_alive()
client = commands.Bot(command_prefix=">",help_command=None,intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'botの起動に成功しました! {client.user}')
    gu=client.guilds
    print(f"サーバー参加数{len(gu)}")
    for gus in gu:
     print(f">>{gus.name}")
    print('---------')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="test"))
    
my_secret = os.environ['.env']
keep_alive.keep_alive()
client.run(my_secret)
