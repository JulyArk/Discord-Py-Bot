from discord.ext import commands
from src.commands.Dictionary.UrbanDict import UrbanDictionary


class DictionaryCog(commands.Cog):
    """
    Finds definitions from UrbanDictionary (mostly for internet slang)
    """

    def __init__(self, bot):
        """
        :param bot: commands.Bot
        """
        self.client = bot

    @commands.command(pass_context=True)
    async def wotd(self, ctx):
        """
        Word of the day on UrbanDictionary
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        msg = UrbanDictionary.word_of_the_day()
        await ctx.message.channel.send(msg)

    @commands.command(pass_context=True)
    async def define(self, ctx):
        """
        UrbanDict definiton of
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        word = " ".join(ctx.message.content.split()[1:])
        msg = UrbanDictionary.define(word)
        await ctx.message.channel.send(msg)


def setup(bot):
    bot.add_cog(DictionaryCog(bot))
