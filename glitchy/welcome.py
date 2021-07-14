from typing import Awaitable, Collection
import discord
from discord import client
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure

class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

botdata = BotData()

class Welcome(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if botdata.welcome_channel != None:
            await botdata.welcome_channel.send(f'Welcome to {member.guild.name}, {member.mention}. ')
            return
        else:
            print('Welcome channel not set, returning.')
            return

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        if botdata.goodbye_channel != None:
            await botdata.goodbye_channel.send(f'Goodbye, {member.mention}. ')
            return
        else:
            print('Goodbye channel not set, returning.')
            return

    @commands.command()
    async def welcome(self, ctx, channel_name=None):
        if channel_name != None:
            for channel in ctx.guild.channels:
                if channel.name == channel_name:
                    botdata.welcome_channel = channel
                    await ctx.channel.send(f'Welcome set. ({channel.name})')
                    await channel.send('This channel has been glitchified. :)')
        else:
            await ctx.send('You didn\'t include a welcome channel name.')

    @commands.command()
    async def goodbye(self, ctx, channel_name=None):
        if channel_name != None:
            for channel in ctx.guild.channels:
                if channel.name == channel_name:
                    botdata.goodbye_channel = channel
                    await ctx.channel.send(f'Goodbye set. ({channel.name})')
                    await channel.send('This channel has been glitchified. :)')
        else:
            await ctx.send('You didn\'t include a goodbye channel name.')

def setup(client):
    client.add_cog(Welcome(client))