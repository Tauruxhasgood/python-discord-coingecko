import os
import discord
from discord.ext import commands

import requests
from requests.exceptions import RequestException


from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('CRYPTO_TOKEN')

api = 'https://api.coingecko.com/api/v3'
   

# client = discord.Client(command_prefix='!')
bot = commands.Bot(command_prefix='%')

coins = ['BTC', 'LTC', 'BCH', 'ETH', 'ETC', 'BAT', 'ZRX', 'USDC', 'XRP',
        'EOS', 'XLM', 'LINK', 'DASH', 'ZEC', 'REP', 'DAI', 'XTZ']

@bot.event
async def on_ready():
    print('Le bot de crypto est prêt !')

@bot.command()
async def list(ctx):
    value = ', '.join(coins)
    embed = discord.Embed(title=value)

    await ctx.send(embed=embed)

bot.run(TOKEN)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('Hello'):
#         await message.channel.send('Bonjour {0.author.mention}'.format(message))

# @client.event
# async def on_ready():
#     print("le bot de crypto est prêt !")



# client.run(TOKEN)
