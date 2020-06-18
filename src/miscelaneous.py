import discord
from discord.ext import commands

import random
from urllib import parse, request
import re

class Miscelaneus(commands.Cog):
    def __init__(self,client):
        self.client = client

    async def on_member_join(self, member):
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
    
    async def on_error(self, event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise

    @commands.Cog.listener()
    async def on_message(self, message):
        author = message.author
        if "consejos para novatos" in message.content.lower():
            url = 'https://www.youtube.com/watch?v=wBQLIWgxs8A&list=PLYg45iMNsrZqe3PfDrivhk2FBZ8ieLO6N&index=9'
            await message.channel.send('{}¿Acabas de empezar? te recomiendo que te mires esto {}'.format(author, url))
            await self.client.process_commands(message)

        if "buenos dias" in message.content.lower():
            await message.channel.send('¡Buenas pollas te comías!')
            await self.client.process_commands(message)

        if "guapos" in message.content.lower():
            await message.channel.send('¡Guapo tu!')
            await self.client.process_commands(message)

    @commands.command(pass_context=True)
    async def info(self, ctx):
        normas = """- En la sala autoranks debes elegir el rango que tienes en competitivo. Esto hará que solo puedas escribir en la sala dirigida a ese rango. De esta manera evitamos saturar de mensajes a todo el mundo.
    
        - No seas tóxico o serás baneado. En este servidor jugamos competitivas, pero lo importante es aprender y seguir avanzando.

        - Está prohibido faltar al respeto a cualquier miembro del canal.
        """
        channel = ctx.message.channel
        embed = discord.Embed(
            title = '¡Bienvenido!',
            description = 'Por favor, lee estas sencillas normas antes de empezar a viciar',
            colour = discord.Colour.blue()
        )

        embed.add_field(name="Normas", value=normas)
        embed.set_image(url="https://static3.thegamerimages.com/wordpress/wp-content/uploads/2020/04/valorant-image-1-2.jpg?q=50&fit=crop&w=963&h=541")
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/8/82/Valorant_Icon.png/revision/latest/scale-to-width-down/20?cb=20200309160959")
        await ctx.send(channel, embed=embed)

    @commands.command(name='99', help='Responde con una frase aleatoria')
    async def nine_nine(self, ctx):
        brooklyn_99_quotes = [
            'Si a los 30 no te has casado, ni a los 40 eres rico. Arre borrico.',
            '¡Chúpamela!',
            'no vea ompare ma dao en to la merla',
            '¡Cabesha pollo!',
        ]

        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)

    @commands.command()
    async def youtube(self, ctx, *, search):
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
        print(search_results)
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

def setup(client):
    client.add_cog(Miscelaneus(client))