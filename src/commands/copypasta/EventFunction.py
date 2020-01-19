from src.commands.copypasta.controller import CopyPastaController
from src.commands.Blacklist.blacklistStorage import Blacklist
from classified.globals import blacklist_file_path
import time
from src.commands.Settings.controller import SettingsController

last_used_time = 0  # A global cooldown time


async def copypasta_on_msg(message):
    """
    Used to check if the message is  copy pasta.
    Full implementation in copypasta
    :param message: Discord.py message Class
    :return: None
    """
    global last_used_time  # Load global
    # Admins get to dodge the cooldown
    if not message.author.top_role.permissions.administrator:
        # If user is not an admin and triggers a copypasta during the cooldown stop executing
        if last_used_time + 15 > time.time():
            return
    if not SettingsController(message.guild).get_setting("copypasta", "respond"):
        return
    pasta_controller = CopyPastaController(message.guild)  # Load the controller

    if message.content in pasta_controller.pastas.pasta_dict:  # If the message is in the dict keys
        contents = pasta_controller.get_dict()[message.content]  # Found
        if contents[1] == 1:  # If bits for the copypasta are set to 1 remove the trigger message
            await message.delete()
        print(pasta_controller.get_dict())
        await message.channel.send(contents[0])  # Print the copypasta
        return


async def blacklistCheck(message):
    blacklistCtr = Blacklist(blacklist_file_path + str(message.channel.guild.id))  # Load the controller
    if blacklistCtr.userExists(message.author.id, message.channel.id):
        await message.delete()
    if blacklistCtr.exists(message.content, message.channel.id):
        await message.delete()
