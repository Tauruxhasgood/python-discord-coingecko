import os
import discord
import requests
import json
import cryptocompare
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()


# TOKEN
TOKEN = os.getenv('CRYPTO_TOKEN')
CRYPTOCOMPARE_API_KEY = os.getenv('CRYPTOCOMPARE')  

# commande qui précèdera l'option voulu
base_command = "!cb"
# channel ou sera écris le résultat
bot_channel = "général"

client = discord.Client()


# mise en place de la card qui s'affichera dans discord
def default_message():
    embed = discord.Embed(
        title=":sunglasses: Crypto Bot",
        description="Ce simple bot suit plusieurs crypto-monnaies en utilisant l'API coinGecko.",
        url="https://github.com/Tauruxhasgood",
        color=0x0FA5F0,
    )
    embed.add_field(name=":money_with_wings: Vérifier les prix", value="```ex: !cb BTC USD```", inline=True)
    embed.add_field(name=".", value="```ex: !cb ETC USD```", inline=True)
    embed.add_field(name=".", value="```ex: !cb SHIB USD```", inline=True)
    embed.add_field(name=":coin: Liste des Crypto", value="```ex: !cb coins```", inline=False)

    embed.add_field(
        name=":chart_with_upwards_trend: Vérifier l'historique des prix",
        value="```ex: !cb history ETH USD 2021/9/23```",
    )
    embed.add_field(
        name=":warning: NOTE:", value="La date minimale est le 20 mars 2017", inline=True
    )
    embed.set_footer(text="made by https://github.com/Tauruxhasgood")
    return embed

# cette partie du code donnera l'historique de la crypto choisit
def price_history(
    command, error_message=None, coin=None, currency=None, timestamp=None
):
    try:
        # on déclare la crypto recherché qui prends la place 2 dans la commande
        # !cb history BTC USD date > !cb = place 0, history = place 1, BTC = place 2, USD = place 3, la date = place 4
        coin = command[2]
        # on déclare la devise voulu, ici en USD qui se trouve en place 3
        currency = command[3]
        # on déclare la date qui se trouve en place 4
        date = [int(x) for x in command[4].split("/")]
        print(date)


        # date_time = datetime.now()
        # str_time = datetime.strftime(date_time, '%d-%m-%Y')
        # print('info str_time', str_time)
        date_time = datetime
        print('info de date_time', date_time)
        
        timestamp = datetime(date[0], date[1], date[2])
        print('info4', timestamp)
        present = datetime.now()
        print('info5', present)

        if timestamp > present:
            timestamp = present
        # Set the minimum date if older than the minimum date
        elif timestamp < datetime(2017, 3, 20):
            timestamp = datetime(2017, 3, 20)
        return coin, currency, timestamp, error_message
    except IndexError:
        error_message = "**ERROR** Invalid number of parameters."
        return coin, currency, timestamp, error_message
    except ValueError:
        error_message = "**ERROR** Invalid parameters."
        return coin, currency, timestamp, error_message


def current_price(command, coin=None, currency=None, error_message=None):
    try:
        coin = command[1]
        currency = command[2]
        return coin, currency, error_message
    except KeyError:
        error_message = "**ERROR** Invalid parameters."
        return coin, currency, error_message



@client.event
async def on_ready():
    print(f"connected as {client.user}")
    await client.change_presence(activity=discord.Game(name="!cb"))

@client.event
async def on_message(message):

    # URL = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false').json()

    if message.author == client.user:
        return
    try:
        if message.content == base_command and message.channel.name == bot_channel:
            embed = default_message()
            await message.channel.send(embed=embed)
        else:
            command = message.content.split(" ")
            # -> prix historique crypto
            if command[1] == "history":
                coin, currency, timestamp, error_message = price_history(command)
                if error_message:
                    await message.channel.send(error_message)
                try:
                    await message.channel.send(
                        f"{coin} Price @ {timestamp.date()}: **{cryptocompare.get_historical_price(coin, currency, timestamp=timestamp)[coin][currency]} {currency}**"
                    )
                except KeyError:
                    await message.channel.send("**ERROR** Invalid parameters.")
            if command[1] == "coins":
                # r = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={arg}&vs_currencies=usd")
                # result = r.json()
                # data = result
                # print(coin)
                
                # for i in range(len(data)): e = data[i]["name"]
                # print(e)
                embed = discord.Embed(
                    title=":coin: Coin List",
                    url="https://www.coingecko.com/fr",
                    description = f"Voici une liste des crypto-monnaies valides que vous pouvez utiliser avec le bot",
                    color=0x29A347,
                )
                embed.set_thumbnail(
                    url=""
                )
                await message.channel.send(embed=embed)
            elif command[1] in cryptocompare.get_coin_list(format=True):
                coin, currency, error_message = current_price(command)
                if error_message:
                     await message.channel.send(error_message)
                try:
                    await message.channel.send(
                        f"Current {coin} Price: **{cryptocompare.get_price(coin, currency)[coin][currency]} {currency}**"
                    )
                except (TypeError, KeyError):
                    await message.channel.send("**ERROR** Invalid parameters.")
    except AttributeError:
        if isinstance(message.channel, discord.channel.DMChannel):
            pass

if __name__ == "__main__":
    client.run(TOKEN)
















# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('Hello'):
#         await message.channel.send('Bonjour {0.author.mention}'.format(message))

# @client.event
# async def on_ready():
#     print("le bot de crypto est prêt !")