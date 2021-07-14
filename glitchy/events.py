from typing import Collection
import discord
from discord import client
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure
import asyncio
from cogwatch import Watcher

async def start_watcher(client):
    watcher = Watcher(client, path="glitchy")
    await watcher.start()


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        asyncio.create_task(start_watcher(self.client))
        
        print("Connecting...")
        await self.client.change_presence(activity=discord.Game(name='Just Monika. | glitch help'))
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
