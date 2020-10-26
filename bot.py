import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

with open("quotes.txt", "r") as f:
    QUOTES = list(
        map(lambda q: q.replace("\n", "").replace("--", "\n--"),
            f.read().split("\n\n")
            )
    )


@bot.event
async def on_ready():
    print(f'{bot.user} as connected to discord!')


@bot.event
async def on_member_join(member):
    print("hiero")
    await member.send("Welcome to the server!")


@bot.command()
async def repeat(ctx, *args):
    response = ""
    for arg in args:
        response += f'{arg} '
    await ctx.channel.send(response.strip())


@bot.command()
async def quote(ctx):
    bot_quote = random.choice(QUOTES)
    await ctx.channel.send(bot_quote)


@bot.command(pass_context=True)
async def nickname(ctx, *args):
    response = ""
    for arg in args:
        response += f'{arg} '
    await ctx.message.author.edit(nick=response)


if __name__ == '__main__':
    bot.run(TOKEN)
