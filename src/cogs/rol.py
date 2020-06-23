import discord
from discord.ext import commands

import random

class Rol(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='roll', help='Simula lanzamiento de dados.')
    async def roll(self,ctx, number_of_dice: int, number_of_sides: int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

def setup(client):
    client.add_cog(Rol(client))