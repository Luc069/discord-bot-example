import nextcord as discord
from nextcord.ext import commands

TOKEN = '#YOUR TOKEN'   https://youtu.be/aI4OmIbkJH8 (How to get it)
client = comands.Bot(command_prefix='!')

@client.command()
async def hello(ctx):
 await ctx.send('hello')
 
 client.run(TOKEN)
