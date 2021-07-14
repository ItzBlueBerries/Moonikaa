from typing import Collection, List
from io import BytesIO
import asyncio
import discord
from discord import client
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure

async def fetch_attachments(attachments: List[discord.Attachment]) -> List[discord.File]:
    return await asyncio.gather(*[attachment.to_file() for attachment in attachments])

class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if not isinstance(message.channel, discord.DMChannel):
            return

        creator_dm_channel = self.client.get_channel(864286535700709376)
        cloned_message = await creator_dm_channel.send(f"__***~~{message.author} (`{message.author.id}`)~~:***__\n```\uFEFF{message.content}```", files=await fetch_attachments(message.attachments))

        def reply_check(m):
            if not m.reference:
                return False

            return m.reference.message_id == cloned_message.id

        reply = await self.client.wait_for("message", check=reply_check)
        await message.reply(reply.content, files=await fetch_attachments(reply.attachments))


def setup(client):
    client.add_cog(Log(client))
