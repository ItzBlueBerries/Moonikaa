from typing import Collection, List
from io import BytesIO
import asyncio
import discord
from discord import client
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import errors
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

        await message.author.send('You\'re DM was successfully sent to the creators, thank you! :)')
        creator_dm_channel = self.client.get_channel(864286535700709376)
        cloned_message = await creator_dm_channel.send(
            f"__***~~{message.author} (`{message.author.id}`)~~ Sent:***__\n```\uFEFF{message.content}```",
            files=await fetch_attachments(message.attachments),
        )

        def reply_check(m):
            if not m.reference:
                return False

            return m.reference.message_id == cloned_message.id

        reply = await self.client.wait_for("message", check=reply_check)
        await message.reply(reply.content, files=await fetch_attachments(reply.attachments))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for chan in member.guild.channels:
            if str(chan) == "welcome-goodbyes-log":
                embed = discord.Embed(title='Welcome Message', description=f'{member} has joined the {member.guild.name}.')
                await chan.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_member_leave(self, member):
        for chan in member.guild.channels:
            if str(chan) == "welcome-goodbyes-log":
                embed = discord.Embed(title='Goodbye Message', description=f'{member} has left {member.guild.name}.')
                await chan.send(embed=embed)


def setup(client):
    client.add_cog(Log(client))
