from typing import Collection
import discord
from discord import client
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure


class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        creator_dm_channel = self.client.get_channel(864286535700709376)
        cloned_message = await creator_dm_channel.send(f"__***~~{message.author} (`{message.author.id}`)~~:***__\n```{message.content}```" + "\n" + "\n".join([a.url for a in message.attachments]))

        def reply_check(m):
            return m.reference.message_id == cloned_message.id

        reply = await self.bot.wait_for("message", check=reply_check)
        await message.reply(reply.content + "\n" + "\n".join([a.url for a in reply.attachments]))


def setup(client):
    client.add_cog(Log(client))
