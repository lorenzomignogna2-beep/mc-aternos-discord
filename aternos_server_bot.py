import discord
import os
from python_aternos import Client
import time

TOKEN = 'MTUzMDIyMzI0MzQyNjkyMjY2Nw.GfqsgD.85j6kd4jNFIXnipFE7LPmL0WO2I74pWbls-KXo'

client = discord.Client()

aternos = Client('L0r3u20', password='Lorenzoscuolamedia')

atservers = aternos.servers

myserv = atservers[0]

@client.event
async def on_ready():
    print('we have logged in a {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-cmnds':
        if user_message.lower() == '?hello':
            await message.channel.send(f'Hello {username}!')
            return

    if message.channel.name == 'bot-cmnds':
        if user_message.lower() == '?server_start':
          myserv.start()
          while True:
            ping = str(os.popen('mcstatus yourservername.aternos.me status | grep description').read())
            if "offline" in ping:
              time.sleep(1)
            else:
              break
          await message.channel.send("server is now alive!!! you can join in 2-3 minutes by pasting ||yourservername.aternos.me:serverport|| in the server address.")
          return

    if message.channel.name == 'bot-cmnds':
        if user_message.lower() == '?server_stop':
          myserv.stop()
          await message.channel.send(f'server stopped')
          return

client.run(TOKEN)
