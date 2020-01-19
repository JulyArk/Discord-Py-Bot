from discord.ext import commands
from src.commands.RateGirl.rategirl import RateGirl
import random


class DiscordRateGirl(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(pass_context=True)
    async def rategirl(self, ctx):
        """
        Rates @User by 2 values, Hot and Crazy
        :param ctx: Context from message
        :return: None
        """
        user_id = float(
            "".join([s for s in ctx.message.content.split()[1] if s.isdigit()]))  # transform user id into a float
        try:
            hot, crazy = RateGirl().rategirl(user_id)  # Call function for pseudo rng
            await ctx.channel.send("Hot: {} Crazy: {}".format(hot, crazy))  # Send formatted message
        except ValueError or ZeroDivisionError:
            pass


def setup(bot):
    bot.add_cog(DiscordRateGirl(bot))
