import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=============")

    await app.change_presence(activity=discord.Game(name="일단은 게임",type=0))

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")

access_tokne = os.environ["BOT_TOKEN"]
client.run(access_token)
