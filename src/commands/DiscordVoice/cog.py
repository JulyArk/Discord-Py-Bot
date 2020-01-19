from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.utils import get


class DiscordBotVoice(commands.Cog):
    """
    A class that handles the bot interaction with voice channels
    """

    def __init__(self, bot):
        self.client = bot

    @commands.command(pass_context=True)
    async def join(self, ctx):
        """
        Bot joins the voice channel the user is in
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        try:
            channel = ctx.message.author.voice.channel
            if not channel:
                await ctx.send("You are not connected to a voice channel")
                return
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                await channel.connect()
        except AttributeError:
            await ctx.send("Your are not connected")

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        """
        Bot leaves voice
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        voice = get(self.client.voice_clients, guild=ctx.guild)
        await voice.disconnect()


def setup(bot):
    bot.add_cog(DiscordBotVoice(bot))
