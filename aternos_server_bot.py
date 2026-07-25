import os
import discord
from python_aternos import Client

# Configurazione Token Discord
TOKEN = 'INSERISCI_QUI_IL_TUO_TOKEN_DI_DISCORD'

# Connessione ad Aternos
atclient = Client()
atclient.login('L0r3u20', 'Lorenzoscuolamedia')
aternos = atclient.account

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot collegato come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_message = str(message.content)

    if message.channel.name == 'bot-cmnds':
        if user_message.lower() == '?hello':
            await message.channel.send("Ciao! Il bot è attivo e pronto.")
            return

        if user_message.lower() == '?server_start':
            await message.channel.send("Sto provando ad accendere il server, attendi...")
            try:
                # Prende il primo server disponibile nell'account
                servs = aternos.list_servers()
                myserver = servs[0]
                myserver.start()
                await message.channel.send("Il server si sta avviando! Potrai entrare tra 2-3 minuti.")
            except Exception as e:
                await message.channel.send(f"Errore durante l'accensione: {str(e)}")
            return

        if user_message.lower() == '?server_stop':
            try:
                servs = aternos.list_servers()
                myserver = servs[0]
                myserver.stop()
                await message.channel.send("Il server è stato spento.")
            except Exception as e:
                await message.channel.send(f"Errore durante lo spegnimento: {str(e)}")
            return

client.run(TOKEN)
