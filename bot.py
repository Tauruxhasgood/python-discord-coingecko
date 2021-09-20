import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# default_intents = discord.Intents.default()
# default_intents.members = True
# client = discord.client(intents=default_intents)

client = discord.Client()
@client.event
async def on_member_join(member):
    general_channel = client.get_channel()
    general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")


client.run(TOKEN)



















# @client.event
# async def on_ready():
#   print("le bot est prêt !")

# @client.event
# async def on_message(message):
#     if message.content == "Ping":
#         await message.channel.send("Pong")