import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

client = Bot(description="Basic Bot by Habchy#1665", command_prefix="PUT YOUR PREFIX HERE", pm_help = True)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    yield from client.change_presence(game=Game(name="This is just for tutorial purposes!"))

@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)
	await client.say(":warning: This bot was created by **Habchy#1665**, it seems that you have not modified it yet. Go edit the file and try it out!")

client.run('MzY1OTU0MDQ2MDkzMjk1NjI4.DOZ7oA.eBP_A8Bul6JL6riBMif_jNYq8Co')
