from src.commands.Reactions.reactions import BotReaction
from classified.globals import reactions_file_path


class ReactionsController:
    """
    Controller for reactions to messages
    """

    def __init__(self, client, guild):
        self.react_dict = BotReaction(reactions_file_path + str(guild.id))
        self.client = client

    def add(self, string: str):
        """
        Adds a reaction to a keyword/keywords
        :param string: message.contents (the literal string of the message)
        :return: status, -1 on invalid input, 0 on already present keyword, 1 on success
        """
        contents = string.split()
        emoji_id = int(''.join(filter(str.isdigit, contents[len(contents) - 1])))
        if self.client.get_emoji(emoji_id) is None:
            return -1
        status = self.react_dict.add_reaction(string)
        if status == 0:
            return 0
        elif status == -1:
            return -1
        self.react_dict.save_dict_to_file()
        return status

    def get(self, key):
        """
        Returns the contents of a key from dict
        :param key: keyword/s
        :return: contents of keyword/s
        """
        return self.react_dict.keywords[key]

    def remove(self, key):
        """
        Removes reaction to key
        :param key: keyword/s
        :return: None
        """
        self.react_dict.remove_reaction(key)
        self.react_dict.save_dict_to_file()

    def get_dict(self):
        """
        Returnss the dict of reactions
        :return: a dictionary
        """
        return self.react_dict.keywords
