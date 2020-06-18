import discord
from discord.ext import commands

import random
from urllib import parse, request
import re

class Miscelaneus(commands.Cog):
    def __init__(self,client):
        self.client = client

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
            'message1',
            'message2',
            'message3',
            'message4',
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