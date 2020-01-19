from discord.ext import commands
from src.commands.Blacklist.controller import BlacklistController
from src.commands.BotMiscellaneous.cog import MiscellaneousCog


class BlacklistCog(commands.Cog):

    def __init__(self, bot):
        self.client = bot
        self.msg = ''
        self.id = -1
        self.controller = None
        self.channel = None

    async def user(self):
        if self.id != -1:
            await self.channel.send(self.controller.add(self.channel.id, 'user', self.id))
        # TODO add finding by nick

    async def message(self):
        await self.channel.send(self.controller.add(self.channel.id, 'message', self.msg.content))
        return

    async def emj(self):
        emjIdList = MiscellaneousCog.findAllNumbersInString(self.msg.content)
        if emjIdList != -1:
            for emojiId in emjIdList:
                await self.channel.send(self.controller.add(self.channel.id, 'emoji', emojiId))
            return

    async def word(self):
        await self.channel.send(self.controller.add(self.channel.id, 'word', self.msg.content.split()[2]))
        return

    @commands.command()
    async def blacklist(self, ctx):
        """
        Example: TODO
        :param ctx: Discord.py Context
        :return: None
        """
        #   Options : user, message, emj, tbd
        options = {'user': self.user, 'message': self.message, 'emoji': self.emj, 'word': self.word}
        self.controller = BlacklistController(ctx.guild)
        self.channel = ctx.channel  # channel in which to ban
        if not ctx.message.author.top_role.permissions.administrator:
            return
        user = ctx.message.content.split()[2]  # raw user string name or nickname
        blacklistType = ctx.message.content.split()[1]  # type of ban

        try:
            self.id = MiscellaneousCog.find_number_in_str(user)  # user id if given by pinging
            if self.id == -1:
                # await self.channel.send("No user found, assuming blacklist word")
                self.id = ctx.message.author.id
        except ValueError:
            pass
        async for message in self.channel.history(limit=50):
            self.msg = message
            if message.author.name == user or message.author.id == self.id:
                await options[blacklistType]()
                return


def setup(bot):
    bot.add_cog(BlacklistCog(bot))
