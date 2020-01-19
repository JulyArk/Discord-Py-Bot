import datetime


def log_chat(file: str, message):
    """
    stores the message contents from discord
    :param file: the name of the file, or a filepath
    :param message: Message class from discord.py
    :return: None
    """
    f = open(file, "a")
    try:
        f.write(message.content + " " + str(message.author) + " " + str(datetime.datetime.now()) + "\n")
        print(message.author.id, message.author.name)
    except UnicodeEncodeError:
        pass
    f.close()
