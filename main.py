import discord
import asyncio as asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game, Server, Member, Embed

client = Bot(description="Basic Bot by Habchy#1665", command_prefix="!", pm_help = True)

@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="dasdasdasdasdasdsad"))

@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)
	await client.say(":warning: This bot was created by **Habchy#1665**, it seems that you have not modified it yet. Go edit the file and try it out!")

client.run('MzY1OTU0MDQ2MDkzMjk1NjI4.DOZ7oA.eBP_A8Bul6JL6riBMif_jNYq8Co')
