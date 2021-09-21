import os
import discord
import requests

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



client = discord.Client(command_prefix='!')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))

@client.event
async def on_ready():
    print("le bot est prêt !")
    print('Connecté en tant que')
    print(client.user.name)
    print(client.user.id)


# x = requests.get('https://api.coingecko.com/api/v3/simple/supported_vs_currencies')
# print(x.text)



# @client.event
# async def on_member_join(member):
#     general_channel = client.get_channel(889435804525547530)
#     general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")


# @client.event
# async def on_message(message):
#     if message.content == "Ping":
#         await message.channel.send("Pong")

client.run(TOKEN)




















