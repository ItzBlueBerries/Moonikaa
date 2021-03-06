import discord
from discord.ext import commands, tasks
import os
from discord.flags import Intents
from dotenv import load_dotenv
import asyncio

intents = discord.Intents.all()

load_dotenv()

GLITCHY_TOKEN = os.getenv("GLITCHY_DISCORD_TOKEN")
GLITCHY_PREFIX = os.getenv("GLITCHY_PREFIX")

client = commands.Bot(command_prefix=GLITCHY_PREFIX + " ", intents=intents)

for filename in os.listdir("./glitchy"):
    if filename.endswith(".py"):
        client.load_extension(f"glitchy.{filename[:-3]}")


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"glitchy.{extension}")
    await ctx.send(f"{extension} has been glitchified. :)")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"glitchy.{extension}")
    await ctx.send(f"{extension} has been unglitchified. :)")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f"glitchy.{extension}")
    client.load_extension(f"glitchy.{extension}")
    await ctx.send(f"{extension} has been reglitchified. :)")


## Testing Events

# @client.event
# async def on_ready():
#     print('Connecting...')
#     await asyncio.sleep(2)
#     print('Hacking into Glitchified Code... :)')
#     await asyncio.sleep(2)
#     print('Connected to API...Moonikaa Speaking, lol. :)')

## Testing

# @client.command()
# async def ping(ctx):
#     await ctx.send('Testing...MOONIKAAAA LOL')

client.run(GLITCHY_TOKEN)
