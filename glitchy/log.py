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
        if message.author == self.client.user:
            return

        empty = []
        channel = self.client.get_channel(864286535700709376)

        creator_dm = self.client.get_channel(864286535700709376)

        if str(message.channel.type) == "private":
            if message.attachments != empty:
                filee = message.attachments[-1]
                await message.author.send('You\'re DM was successfully sent to the creators, thank you! :)')
                await creator_dm.send(f'__***~~ {message.author} ({message.author.id}) ~~ Sent:***__')

                for file in filee:
                    await creator_dm.send(f'{filee.url}')
            # creator_dm = discord.utils.get(self.client.get_all_channels(), guild__name='Fruitsy Bot Testing Server', name='dms-for-the-creator')
            else:
                await message.author.send('You\'re DM was successfully sent to the creators, thank you! :)')
                await creator_dm.send(f'__***~~ {message.author} ({message.author.id}) ~~ Sent:***__\n```{message.content}```')
        # elif str(message.channel) == channel and message.content.startsWith("<"):
        #     member_obj = message.mentions[0]

        #     index = message.content.index(" ")
        #     string = message.content()
        #     dm_message = string[index:]

        #     await member_obj.send(f'__***~~ {message.author} ({message.author.id}) ~~ Sent Back:***__\n```{dm_message}```')

def setup(client):
    client.add_cog(Log(client))