from typing import Collection
import discord
from discord import client
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure

class Delete(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def placeholder(self, ctx):
        await ctx.send('ez')
        return

def setup(client):
    client.add_cog(Delete(client))