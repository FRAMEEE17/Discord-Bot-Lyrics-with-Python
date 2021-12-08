import discord
from discord.ext import commands

import json
import requests
from lyrics_api import *


bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
  print('connected to bot:{}'.format(bot.user.name))
  print('BOT ID:{}'.format(bot.user.id))



@bot.command()
async def Title(ctx):
  await ctx.message.delete()
  mention = ctx.author.mention

  emBedlyrics=discord.Embed(title=f'Welcome to the Musixmatch Lyrics!', description=f'resquest by [{mention}]', color= 0x03f8fc)
  emBedlyrics=discord.Embed(title=f'Press a key message and then will go through the lyrics', description=f'resquest by [{mention}]', color= 0x7289da)
  emBedlyrics.add_field(name='Name of Artist 🚀', value='pls type an artist to which you want ')
  emBedlyrics.add_field(name='Name of Track🔥',value='pls search the track or name of a song')
  emBedlyrics.add_field(name='Lyrics🎸',value='the lyrics will display in discord')
  emBedlyrics.set_thumbnail(url = 'https://cdn.discordapp.com/icons/282219466589208576/fe3dc9095267b415b70f61419f4166a8.png')
  emBedlyrics.add_field(name='🖲 Press  $Lyrics ',value='(✿◕‿◕✿)   For zero or call',inline=True)
  emBedlyrics.add_field(name='🖱 Press  $zero ', value='.·´¯`(>▂<)´¯`·.      For Exit',inline=True)
  emBedlyrics.add_field(name='🖲 Press  $call ', value='(〜￣▽￣)〜            For Lyrics',inline=True)
  
  
  
  await ctx.channel.send(embed=emBedlyrics)

@bot.command()
async def Lyrics(ctx):
  typing = ctx.channel.send #ต้องเปลี่ยน send เป็นอะไรสักอย่าง
  choice = str
  await ctx.channel.send("$zero or $call ")
  while True:
    await typing(str) == choice
    print(choice)
    if choice == "$zero":
        break
    if choice == "$call":
      await  ctx.channel.send("Whats's the name of the artist?")
      await typing(str ) == artist_name #ใช้คำสั่งinputในดิสคอร์ด
      print(artist_name)
      await ctx.channel.send("What's the name of the track?")
      await typing(str) == track_name #ใช้คำสั่งinputในดิสคอร์ด
      print(track_name)
      
      
  
      api_call = base_url + lyrics_matcher + format_url + artist_search_parameter  + artist_name + track_search_parameter  + track_name + api_key
      request = requests.get(api_call)
      data = request.json()
      data = data['message']['body']
      await ctx.channel.send(data['lyrics']['lyrics_body'])
      await ctx.channel.send("API Call: " + api_call)
      #request = requests.get("https://discord.com/api/path/to/the/endpoint")
    
bot.run("TOKEN")