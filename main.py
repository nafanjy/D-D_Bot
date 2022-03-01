import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json
import os
import functions
import vars
from keep_alive import keep_alive
import youtube_dl



client = commands.Bot(command_prefix = '!')

#log in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


  
#look at messages on the server
@client.event
async def on_message(message):
  #message author name
    author = str(message.author.display_name)
    if '#' in author:
        author = author.split("#", 1)
        author = author[0]
  #ignore myself
    if message.author == client.user:
        return

  #conversations
    if message.content.startswith('hey, bot'):
        string = functions.conversation(author)
        await message.channel.send(string)

  #roll dice
    if message.content.startswith('!r'):
        remove_command_str = str(message.content).strip('!roll').strip().rstrip()
        response_str = functions.roll(remove_command_str)
        await message.channel.send(response_str)

  #feeling sad
    if any(word in message.content for word in vars.sad_words) and ('I ' or 'i ' in message.content):
        happy_str = functions.feeling_sad(author)
        await message.channel.send(happy_str)
  #voice channel
    #join
    if message.content.startswith('!bj'):
        channel = client.get_channel(message.author.voice.channel.id)
        await channel.connect()
    #leave
    if message.content.startswith('!bl'):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                await vc.disconnect()
    #play
    #this does not work in replit
    #the download takes too long to be viable and dependencies are not avilable for dl
    if message.content.startswith('!play'):
        url_input = str(message.content).strip('!play').strip().rstrip()
        channel = client.get_channel(message.author.voice.channel.id)
        voice = await channel.connect()
  
        ydl_opts = {
          'format': 'bestaudio/best',
          'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
          }],
        }
  
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url_input])
        for file in os.listdir("./"):
          if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
  
        source = FFmpegPCMAudio('song.mp3')
        player = voice.play(source)
        
      

#run with secret token
keep_alive()
client.run(os.getenv('TOKEN'))
