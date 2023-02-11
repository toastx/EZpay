import hikari
import lightbulb
import string
import os
import requests
import logging
import datetime
from db import databse

from dotenv import load_dotenv
load_dotenv()


#logging
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("requests.packages.urllib3").setLevel(logging.CRITICAL)


#setup
times= datetime.datetime.now()
times = times.strftime("%D")
token = os.getenv("discordBotToken")
channel = os.getenv("channelID")
bot = lightbulb.BotApp(token = token, prefix = "!")
footer = f"Powered by EZPay   •   {times}"



#command

# @bot.command
# @lightbulb.command("add","add uid")
# @lightbulb.implements(lightbulb.PrefixCommand)

@bot.command
@lightbulb.option("domain",".mag domain")
@lightbulb.command("bal", "show bal")
@lightbulb.implements(lightbulb.PrefixCommand)
async def showBalance(ctx):
    dct = {}
    print(databse)
    for i in databse:
        if i['domain'] == str(ctx.options.domain):
            dct = i
    embed = hikari.Embed(
        title=f':arrow_right: **BALANCE**',
        description=
        f" **Sol** \n **{dct['accountBalance']['sol']} ** \n\n"
        f" **Btc** \n ** {dct['accountBalance']['btc']}** \n\n"
        f" **Bnb** \n **{dct['accountBalance']['bnb']} **\n\n"
        f" **Eth** \n **{dct['accountBalance']['eth']}**\n\n "
        f" **trc** \n **{dct['accountBalance']['trc']}**\n\n ",
        color="#151b2e"
        )
    embed.set_footer(footer)

    await bot.rest.create_message(channel=channel, embed=embed)

# @bot.command
# @lightbulb.command("txns", "shows last 10 txns")
# @lightbulb.implements(lightbulb.PrefixCommand)
# async def showTXNS(ctx):
#     await



@bot.command
@lightbulb.command("ping", "p")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx):
    embed = hikari.Embed(
        title = "test",
        description = "pong",
    )
    await bot.rest.create_message(channel=channel,embed=embed)

@bot.command
@lightbulb.option("coinprice", "enter coin name", type=str)
@lightbulb.command("crypto", "price of coin")
@lightbulb.implements(lightbulb.PrefixCommand)
async def crypto(ctx):
    url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={str(ctx.options.coinprice)}&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    coindata = response.json()
    price = coindata[0]['current_price']
    pricechange24hr = coindata[0]['price_change_percentage_24h']
    high24hr = coindata[0]['high_24h']
    low24hr = coindata[0]['low_24h']
    stonks = ''
    if pricechange24hr >= 0:
        color1 = "#66FF00"
    if pricechange24hr < 0:
        color1 = "#FF0000"

    embed = hikari.Embed(
        title=f"**{price} $ ({float(round(pricechange24hr,2))} %)** {stonks}",
        description=f"** 24hr high** ➤ **{high24hr} $**\n\n** 24hr low  ** ➤ **{low24hr} $**\n\n",
        color=color1
    )
    embed.set_author(name=f"{str(ctx.options.coinprice).capitalize()}", icon=coindata[0]['image'])
    embed.set_footer(footer)
    await bot.rest.create_message(channel= channel, embed=embed)    

bot.run()




