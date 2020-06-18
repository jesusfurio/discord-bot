import discord
from discord.ext import commands

from os import environ

TOKEN = 'YOUR_TOKEN'

startup_extensions = ["valorant","music", "rol","miscelaneous"]

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    activity =discord.Game(name='VALORANT')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print("My bot is ready and connected")

if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    client.run(TOKEN)