from src.commands.Reactions.controller import ReactionsController
from src.commands.Settings.controller import SettingsController


async def react_to_msg(message, client):
    """
    Used to check message contents for keywords. Adds a specified reaction on a message.
    Full implementation in Reactions
    :param message: Discord.py Message class
    :param client: bot from commands.Bot
    :return: None
    """
    if not SettingsController(message.guild).get_setting("reactions", "react"):
        return
    try:

        reaction_controller = ReactionsController(client, message.guild)  # Create the controller
        # reaction_controller.react_dict.import_guild_reactions("reactions_pickle.txt") # if you need to import reacts
        dict_r = reaction_controller.get_dict()  # Get the dictionary
        for key in dict_r:
            if message.content.find(key) != -1:  # If the message is found in the text of the message add the reaction
                await message.add_reaction(client.get_emoji(dict_r[key]))
                return
    except Exception:
        print("Something went wrong")
