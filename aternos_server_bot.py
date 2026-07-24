import discord
import os
from python_aternos import Client
import time

TOKEN = '60b5e404268f1c650b7c16bf85dd74b9c7d995f3c328180379ab37a759ff4a5f'

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
