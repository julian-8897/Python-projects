import discord


class CustomClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 934280435503075338

    async def on_ready(self):
        print('READY')

    async def on_raw_reaction_add(self, payload):
        """
        Provide a role based on the reaction emojis 
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name='Role 1')
            await payload.member.add_roles(role)

        elif payload.emoji.name == '🙌':
            role = discord.utils.get(guild.roles, name='Role 2')
            await payload.member.add_roles(role)

        elif payload.emoji.name == '👊':
            role = discord.utils.get(guild.roles, name='Role 3')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove role based on removed reaction emoji 
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name='Role 1')
            await member.remove_roles(role)

        elif payload.emoji.name == '🙌':
            role = discord.utils.get(guild.roles, name='Role 2')
            await member.remove_roles(role)

        elif payload.emoji.name == '👊':
            role = discord.utils.get(guild.roles, name='Role 3')
            await member.remove_roles(role)


intents = discord.Intents.default()
intents.members = True

client = CustomClient(intents=intents)
client.run('OTM0MjM0NjIwNDIwMDMwNDY0.YetHyg.8fHV_iLbK44pmT61axDKc4Zs8Ps')
