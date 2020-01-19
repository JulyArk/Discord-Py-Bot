import requests
from bs4 import BeautifulSoup


# TODO clean define
class UrbanDictionary:
    # returns word specified in argument
    @staticmethod
    def define(word: str):
        """
        Searches for the definition of a word/sentence on Urban Dictionary using BeautifulSoup for web scraping
        :param word: the string to find definition for
        :return: The definition of the message, formatted
        """
        try:
            r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))  # goes to link for word
            soup = BeautifulSoup(r.content, features="html.parser")  # sets up soup
            def_header = "**" + soup.find("div", attrs={"class": "def-header"}).text.replace("unknown",
                                                                                             "") + "**"
            # header is the word we are defining
            meaning = soup.find("div", attrs={"class": "meaning"}).text  # gets the definition
            for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                meaning = meaning.replace(str(x) + ". ", "\n" + str(x) + ". ")
            meaning = "```" + meaning + "```"
            example = soup.find("div", attrs={"class": "example"}).text  # gets the example
            for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                example = example.replace(str(x) + ". ", "\n" + str(x) + ". ")
            output = def_header + ": " + meaning + " " + "\nExample: " + "```" + example + "```"  # output string
            output = output.replace("&apos", "'")  # replaces weird formatting of ' from original
            return output  # returns the word, defintion, and example
        except AttributeError:
            return "No results"

    # returns the word of the day from the homepage
    @staticmethod
    def word_of_the_day():
        """
        The word of the day on Urban Dictionary
        :return: The definition of the word of the day, formatted
        """
        r = requests.get("http://www.urbandictionary.com")  # link is always homepage
        soup = BeautifulSoup(r.content, features="html.parser")  # sets up soup
        def_header = "**" + soup.find("div", attrs={"class": "def-header"}).text.replace("unknown",
                                                                                         "") + "**"  # header is the word we are defining
        # def_header = def_header[0:len(def_header) - 10]  # header always ends in "unknown" this removes it
        meaning = soup.find("div", attrs={"class": "meaning"}).text  # gets the definition
        # formatting TODO move to controller
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            meaning = meaning.replace(str(x) + ". ", "\n" + str(x) + ". ")
        for x in ["v.", "n."]:
            meaning = meaning.replace(x, x.upper()[:-1])
        example = soup.find("div", attrs={"class": "example"}).text  # gets the example
        output = def_header + ": " + "```" + meaning + "\nEx: " + example + "```"  # output string
        output = output.replace("&apos", "'")  # replaces weird formatting of ' from original
        return output  # returns the word, defintion, and example
