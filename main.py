import discord
import asyncio
from discord import Game, Server, Member, Embed

@client.event
async def on_ready():
	print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="This is just for tutorial purposes!"))

client.run('MzY1OTU0MDQ2MDkzMjk1NjI4.DOZ7oA.eBP_A8Bul6JL6riBMif_jNYq8Co')
