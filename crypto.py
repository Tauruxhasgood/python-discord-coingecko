import os
import discord
import requests
import json


from dotenv import load_dotenv
URL = requests.get('https://api.coingecko.com/api/v3/coins/list')

load_dotenv()
TOKEN = os.getenv('CRYPTO_TOKEN')
# CRYPTOCOMPARE_API_KEY = os.getenv('CRYPTOCOMPARE')  

# commande qui précèdera l'option voulu
base_command = "!cb"
# channel ou sera écris le résultat
bot_channel = "général"

client = discord.Client()


# mise en place de la card qui s'affichera dans discord
def default_message():
    embed = discord.Embed(
        title=":sunglasses: Crypto Bot",
        description="This simple bot tracks several cryptocurrencies using the coinGecko API",
        url="https://github.com/Tauruxhasgood",
        color=0x0FA5F0,
    )
    embed.add_field(name=":money_with_wings: Check Prices", value="```!cb BTC USD```")
    # embed.add_field(
    #     name=":chart_with_upwards_trend: Check Historical Prices",
    #     value="```!cb history ETH EUR 2021/9/23```",
    # )
    embed.add_field(name=":coin: Coin List", value="```!cb coins```")
    embed.set_footer(text="made by https://github.com/Tauruxhasgood")
    return embed

# def price_history(
#     command, error_message=None, coin=None, currency=None, timestamp=None
# ):
#     try:
#         coin = command[2]
#         currency = command[3]
#         date = [int(x) for x in command[4].split(",")]
#         timestamp = datetime(date[0], date[1], date[2])
#         present = datetime.now()
#         if timestamp > present:
#             timestamp = present
#         # Set the minimum date if older than the minimum date
#         elif timestamp < datetime(2020, 3, 20):
#             timestamp = datetime(2020, 3, 20)
#         return coin, currency, timestamp, error_message
#     except IndexError:
#         error_message = "**ERROR** Invalid number of parameters."
#         return coin, currency, timestamp, error_message
#     except ValueError:
#         error_message = "**ERROR** Invalid parameters."
#         return coin, currency, timestamp, error_message


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
    if message.author == client.user:
        return
    try:
        if message.content == base_command and message.channel.name == bot_channel:
            embed = default_message()
            await message.channel.send(embed=embed)
        else:
            command = message.content.split(" ")
            # -> prix historique crypto
            # if command[1] == "history":
            #     coin, currency, timestamp, error_message = price_history(command)
            #     if error_message:
            #         await message.channel.send(error_message)
            #     try:
            #         await message.channel.send(
            #             f"{coin} Price @ {timestamp.date()}: **{URL.get_historical_price(coin, currency, timestamp=timestamp)[coin][currency]} {currency}**"
            #         )
            #     except KeyError:
            #         await message.channel.send("**ERROR** Invalid parameters.")
            if command[1] == "coins":
                r = requests.get('https://api.coingecko.com/api/v3/coins/list')
                result = r.json()
                data = result
                
                for i in range(len(data)): e = data[i]["name"]
                print(e)




                embed = discord.Embed(
                    title=":coin: Coin List",
                    url="https://www.coingecko.com/fr",
                    description = f"{e}",
                    color=0x29A347,
                )
                embed.set_thumbnail(
                    url=""
                )
                await message.channel.send(embed=embed)
            elif command[1] in URL.get_coin_list(format=True):
                coin, currency, error_message = current_price(command)
                if error_message:
                     await message.channel.send(error_message)
                try:
                    await message.channel.send(
                        f"Current {coin} Price: **{URL.get_price(coin, currency)[coin][currency]} {currency}**"
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