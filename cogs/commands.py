from discord.ext import commands
from selenium import webdriver
import snscrape.modules.twitter as sntwitter
import discord
from sheets.test3 import get_tweets_intoDF, showPercentage, best
from sheets.search import search_for_user
#import sheets.search
#import sheets.append




class AppCommands(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Bot is ready!")

  @commands.command()
  async def ping(self, ctx):
    bot_latency = round(self.client.latency * 1000)
    await ctx.send(f"Pong! {bot_latency} ms.")

  @commands.command()
  async def embed(self, ctx, arg1):    
    try:
      profile = enumerate(sntwitter.TwitterSearchScraper(f'from:{arg1}').get_items())

      for i, tweet in profile:
        embed_message = discord.Embed(title=f"{arg1}'s twitter stats",description=f"requested by {ctx.author.mention}")
      
        embed_message.set_image(url=tweet.user.profileImageUrl)
        embed_message.add_field(name='Followers', value=f'{tweet.user.followersCount:,}', inline=False)
        embed_message.add_field(name='Friends', value=f'{tweet.user.friendsCount:,}', inline=False)
        await ctx.send(embed = embed_message)
        break      

    except:
        await ctx.send(f"{arg1}'s profile could not be found")

  @commands.command()
  async def test(self, ctx, arg1, arg2):
    await ctx.send(arg1)

  @commands.command()
  async def read(self, ctx, arg1, arg2): #arg1 = userName, #arg2 = tweet count
    # if sheets.search.search_for_user(arg1) == None:
    #   get_tweets_intoDF(arg1, arg2)


    # await ctx.send('added content')
    file = open('/Users/pham/Desktop/Coding/Project/discord-bot/input.txt', "r")
    content = file.read()
    file.close()
    await ctx.send(content)


  # async def notembed(self, ctx, arg1):
  #   embed_message = discord.Embed(title="title",description="description")
  #   embed_message.set_author(name="thomas")
  #   embed_message.set_thumbnail(url=ctx.guild.icon)
  #   embed_message.add_field(name="temp", value=arg1)
  #   await ctx.send(embed = embed_message)
      

async def setup(client):
  await client.add_cog(AppCommands(client))