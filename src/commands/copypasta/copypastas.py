import pickle


class CopyPastas:
    """
    A Class meant to store bot replies to certain words/ sentences
    Eg:
    .addpasta abc "def" 1
    -User types: "abc"
    -Bot responds with: "def"
    -Number at the end is the bit that decides if the trigger message (abc) gets deleted
    """

    def __init__(self, path):
        """
        A file path where to store the dictionary of copypastas in a pickle format
        :param path: file name or true path
        """
        self.file_path = path  # Dictionary picke location
        self.pasta_dict = self.load_dict_from_file()
        if self.pasta_dict is None:  # No dict found, make an empty one
            self.pasta_dict = {}

    @staticmethod
    def get_the_pasta(string: str):
        """

        :param string: receives a message.context (a string) and formats the contents ass a pasta
        :return: keymark (key) to be added in dictionary containing pasta (message)
        """
        try:

            keymark = string.split()  # Split the message text received into a string of words
            keymark.pop(0)  # Remove the command (.addpasta, .eatpasta, etc)
            # Add the words together and make the key everything before char(")
            keymark = " ".join(keymark).split('"')[0]
            keymark = keymark[:-1]  # Remove space from the end
            pasta = string.split('"')[1]  # everything inside the " " gets selected as the pasta
            bits = int(string.split('"')[2])  # everything after (just 0 or 1) becomes the bit
        except IndexError:
            keymark = None
            pasta = None
            bits = None
        if bits is None:  # If no bits are specified at the end they're automatically set to 1
            bits = 1
        return keymark, pasta, bits

    def save_dict_to_file(self):
        """
        Saves the dictionary to the file
        """
        file = open(self.file_path, "wb")
        pickle.dump(self.pasta_dict, file)
        file.close()

    def load_dict_from_file(self):
        """
        Loads the dictionary from the file
        """
        try:
            file = open(self.file_path, "rb")
            dict_holder = pickle.load(file)
            file.close()
            return dict_holder
        except EOFError:  # Dictionary file exists but it's empty or a bunch of spaces
            self.pasta_dict = {}
        except FileNotFoundError:  # Dictionary file doesnt exist
            file = open(self.file_path, "wb")
            file.close()

    def add_pasta(self, string: str):
        """
        Adds a copypasta
        :param string: message.or the full discord message from the user
        :return: status of the action -1 for invalid input, 0 for already present and 1 for success
        """
        key, pasta, bits = self.get_the_pasta(string)  # Parse data into parts
        if key is None:  # Validation
            return -1
        elif key in self.pasta_dict:  # Validation
            return 0
        if not self.test_pasta_text(pasta):  # Validation
            return -1
        self.pasta_dict[key] = [pasta, bits]  # Add it to dictionary
        return 1

    def removeSauce(self, key: str):
        key = key.split()  # Split the message text obtained into a list of words
        key.pop(0)  # Remove the command part (.eatpasta)
        key = " ".join(key)  # Create the full key in a string
        print(key)
        # self.pasta_dict.pop('<:Worry:583048917910814750>')
        # self.pasta_dict.pop('<:PepeWhip:582391831690739720>')
        for value in self.pasta_dict:
            if self.pasta_dict[value][0] == key:
                print(self.pasta_dict[value][0])  # Remove the copypasta
                self.pasta_dict.pop([value][0])

                return 1
        return -1

    def remove_pasta(self, key: str):
        """
        Removes a copypasta
        :param key: the key of the message
        :return: status of the action, 0 for invalid input, -1 for not found, 1 for success
        """
        key = key.split()  # Split the message text obtained into a list of words
        key.pop(0)  # Remove the command part (.eatpasta)
        key = " ".join(key)  # Create the full key in a string

        if key is None:  # Validation
            return 0
        elif key not in self.pasta_dict:  # Validation
            return -1
        self.pasta_dict.pop(key)  # Remove the copypasta
        return 1

    @staticmethod
    def test_pasta_text(pasta):
        """
        Checks if the message contents are good
        :param pasta: the message that gets sent by typing a key
        :return: True or False
        """
        if len(pasta) > 200:
            return False
        elif len(pasta) < 3:
            return False
        return True

    def update_to_access_bits(self):
        """
        This function is only used if the dictionary isn't made from lists ( from the old version )
        to change it to a proper setup. Mainly ignore.
        :return:
        """
        for pasta in self.pasta_dict:
            x = self.pasta_dict[pasta]
            self.pasta_dict[pasta] = [x, 1]
        self.save_dict_to_file()
        print(self.pasta_dict)

    def set_bits_value(self, msg):
        """
        Set the bit that decides if the keyword message gets deleted or not
        Command eg: .pastabits abc | 1
        - abc = key
        - | = delimiter
        - 1 bit gets set to
        :param msg: Message text
        :return: True/False
        """
        try:
            key = msg.split('|')[0][:-1]  # Obtain the key
            bits = int(msg.split('|')[1])  # Obtain the bit
            self.pasta_dict[key][1] = bits
            self.save_dict_to_file()
            return True
        except KeyError:  # Key not found
            return False

    def import_guild_pastas(self, filename):
        """
        This is made in case you want to import pastas from another file
        :param filename: name of the file (must be a pickle)
        :return: None
        """
        file = open(filename, "rb")
        dict_holder = pickle.load(file)
        self.pasta_dict = dict_holder
        self.save_dict_to_file()
