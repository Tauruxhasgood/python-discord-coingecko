import json
import os
import discord
import requests
import feedparser
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('ACTU_TOKEN')

client = commands.Bot(command_prefix="!")


# url = "https://worldofwarcraft.judgehype.com/nouvelles.xml"
url = "https://korben.info/feed"

feed = feedparser.parse(url)


def extract_item(item):
    result = {}
    for entry in feed.entries:
        # Titre
        title = entry.title
        # print('info 1', title)
        # Date de publication
        published = entry.published
        # print('info 2', published)
        # Permalink
        link = entry.link
        # print('info 3', link)
        # Description sommaire
        # summary = entry.summary
        # print('info 4', summary)
        # Le contenu HTML
        description = entry.description
        # print('info 5', description)
        # print('')


@client.command()
async def on_ready():
    # information pour savoir si le bot est correctement connecté
    print(f'connected as {client.user}')

@client.command()
async def embed(ctx):
    
    embed=discord.Embed(
        title="Judgehype",
        url="https://worldofwarcraft.judgehype.com/",
        color=0x0FA5F0,
    )
    # embed.set_author(
    #     name= ctx.author.display_name,
    #     url="https://twitter.com/RealDrewData",
    #     icon_url= ctx.author.avatar_url
    # )

    embed.set_footer(text="made by https://github.com/Tauruxhasgood")
    await ctx.send(embed=embed)





























client.run(TOKEN)