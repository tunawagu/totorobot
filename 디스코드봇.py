import asyncio
import discord
import time
import random
import datetime
import os

app = discord.Client()
token = "NjYwMTI0NjE4MzYyODQ3MjQz.XgYs_w.xHnQ2NMKF9mF8tGNtNiaZLu763I"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=============")

    await app.change_presence(activity=discord.Game(name="일단은 게임",type=0))

@app.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "토토로 뭐해":
        await message.channel.send("지금은 게임중")

    if message.content == "토토로 나가":
        await message.channel.send("넹 T^T")

    elif message.content == "!바보":
        await app.send_message(message.channel, random.choice(["어쩌라고","뉘에뉘에", "그러든지, 말든지..."]))
app.run(token)
