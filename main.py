import discord
import os
import functions
import vars
from keep_alive import keep_alive



client = discord.Client()

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

#run with secret token
keep_alive()
client.run(os.getenv('TOKEN'))
