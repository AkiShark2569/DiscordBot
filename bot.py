import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("おはよう"):
        if client.user != message.author:
            m = "おはようございます" + message.author.name + "さん！"
            await message.channel.send(m)

client.run("NjA2MzY4NTkxOTEwMjczMDI0.XUKC6Q.fXw7x4PrbmFV0F8tD0EFf_DXIlo")