import os
import asyncio
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="=", intents = discord.Intents.all())

TOKEN = "MTA3MTgxNTQ2NTQ2MDA1MTk5OA.GtTzZG.HnrJPTcp6e5jBqPlTSE4K2mnr4Klt4JXEobSXs"

@client.event
async def on_ready():
  print("Bot is connected to discord")

async def load():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
  async with client:
    await load()
    await client.start(TOKEN)


asyncio.run(main())