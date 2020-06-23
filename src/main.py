import discord
from discord.ext import commands

import os

TOKEN = os.environ.get('TOKEN')

startup_extensions = ["valorant","music", "rol","miscelaneous"]

client = commands.Bot(command_prefix = '!')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Hierro')
    await member.add_roles(role)

    normas = """- En la sala autoranks debes elegir el rango que tienes en competitivo. Esto hará que solo puedas escribir en la sala dirigida a ese rango. De esta manera evitamos saturar de mensajes a todo el mundo.
    
    - No seas tóxico o serás baneado. En este servidor jugamos competitivas, pero lo importante es aprender y seguir avanzando.

    - Está prohibido faltar al respeto a cualquier miembro del canal.
    """
    embed = discord.Embed(
        title = f'¡Bienvenido!',
        description = 'Por favor, lee estas sencillas normas antes de empezar a viciar',
        colour = discord.Colour.blue()
    )

    embed.add_field(name="Normas", value=normas)
    embed.set_image(url="https://static3.thegamerimages.com/wordpress/wp-content/uploads/2020/04/valorant-image-1-2.jpg?q=50&fit=crop&w=963&h=541")
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/8/82/Valorant_Icon.png/revision/latest/scale-to-width-down/20?cb=20200309160959")

    for channel in member.guild.channels:
        if str(channel) == "bienvenido":
            await channel.send(f'{member.mention}',embed=embed)

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