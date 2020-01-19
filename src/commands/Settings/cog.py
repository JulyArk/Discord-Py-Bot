from discord.ext import commands
from src.commands.Settings.controller import SettingsController


class Settings(commands.Cog):
    def __init__(self, bot):
        self.client = bot
        self.functionMap = {"add": self.add, "update": self.update, "reset": self.reset, "get": self.get}
        self.controller = None
        self.jsonString = ""
        self.ctx = None

    def generate_controller(self, guild):
        self.controller = SettingsController(guild)

    def add(self):
        self.controller.add(self.jsonString)
        return "Updated"

    def update(self):
        self.controller.update(self.jsonString)
        return "Added"

    def reset(self):
        self.controller.remove(self.jsonString)
        return "Reset successful"

    def get(self):
        return "```\n" + self.controller.get() + "\n```"

    @commands.command()
    async def settings(self, ctx):
        if not ctx.message.author.top_role.permissions.administrator:
            return
        option = ctx.message.content.split()[1]
        self.ctx = ctx
        self.jsonString = " ".join(ctx.message.content.split()[2:])
        # print(option)
        # print(self.jsonString)
        self.generate_controller(ctx.guild)
        result = self.functionMap[option]()
        if result:
            await self.ctx.channel.send(result)


def setup(bot):
    """
    Required for the functionality of cog
    :param bot: commands.Bot
    :return: None
    """
    bot.add_cog(Settings(bot))
