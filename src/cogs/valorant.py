import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class Valorant(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def weapon(self, ctx, weapon):
        channel = ctx.message.channel

        url = 'https://valorant.fandom.com/wiki/{}'.format(weapon)
        page_response = requests.get(url, timeout = 5)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        name = page_content.find('h2', class_='pi-item pi-item-spacing pi-title').getText()
        weapon = page_content.find('a', class_='mw-redirect').getText()
        image = page_content.find('a',class_='image image-thumbnail')

        damage_values = page_content.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
        records = []
        for row in damage_values:
            penetration = row.find('div',class_="pi-data-value pi-font").text
            records.append((penetration))

        damage = page_content.find_all('table', class_='pi-horizontal-group')
        records_header = []
        for column in damage:
            head = page_content.find_all('thead')
            for header in head:
                column = column.find_all('th')
                for value in column:
                    records_header.append((value.get_text()))

        records_body = []
        for row in damage:
            body = page_content.find_all('tbody')
            for rows in body:
                final_values1 = row.find('td').text
                records_body.append(final_values1)
        
        primary = """Mode: {}
        Fire Rate: {}""".format(str(records[4:5]),str(records[5:6]))

        alternative = """Zoom Mode: {}
        Fire Rate: {}""".format(str(records[6:7]),str(records[7:8]))

        embed = discord.Embed(
            title = name,
            description = weapon,
            colour = discord.Colour.red()
        )
    
        embed.add_field(name="Primary", value=primary)
        embed.add_field(name="Alternative", value=alternative)
        embed.add_field(name="Distance damage", value=str(records_header[0:1]), inline=False)
        embed.add_field(name="Damages", value=str(records_body[0:1]))
        embed.set_image(url=str(image['href']))
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/8/82/Valorant_Icon.png/revision/latest/scale-to-width-down/20?cb=20200309160959")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Valorant(client))