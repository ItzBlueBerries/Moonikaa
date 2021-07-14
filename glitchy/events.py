from typing import Collection
import discord
from discord import client
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure
import asyncio
from cogwatch import watch


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Connecting...")
        await asyncio.sleep(2)
        print("Hacking into Glitchified Code... :)")
        await asyncio.sleep(2)
        print("Connected to API...Moonikaa Speaking, lol. :)")

    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Disconnecting...")
        await asyncio.sleep(2)
        print("Unhacking into Glitchified Code... :(")
        await asyncio.sleep(2)
        print("Disconnected to API...Moonikaa Leaving, oof. :(")


def setup(client):
    client.add_cog(Events(client))
