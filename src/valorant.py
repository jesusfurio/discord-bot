import discord
from discord.ext import commands

class Valorant(commands.Cog):
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

def setup(client):
    client.add_cog(Valorant(client))