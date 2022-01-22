import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Are you ready to RUMBBBLLEEE')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'cool':
        await message.add_reaction('\U0001F920')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

client.run('OTM0MjM0NjIwNDIwMDMwNDY0.YetHyg.vTFYFfccdvlszZTO6H6SCZwofbA')
