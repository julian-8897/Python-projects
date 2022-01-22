import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Are you ready to RUMBBBLLEEE')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Welcome to the channel!')

client.run('OTM0MjM0NjIwNDIwMDMwNDY0.YetHyg.8fHV_iLbK44pmT61axDKc4Zs8Ps')
