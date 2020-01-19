import urllib
import random
from bs4 import BeautifulSoup


class YouTube:
    """
    Searches youtube for videos using the BeautifulSoup Library
    """
    @staticmethod
    def find_first(query):
        """
        Fint the first result from youtube
        :param query: topic to look for
        :return: link/url to the video
        """
        query = urllib.parse.quote(query)
        url = "https://www.youtube.com/results?search_query=" + query
        respone = urllib.request.urlopen(url)
        html = respone.read()
        soup = BeautifulSoup(html, 'html.parser')
        res = soup.find_all(attrs={"class": "yt-uix-tile-link"})[0]['href']
        if len(res) > 20 or res.find("user")!= -1:
            res = soup.find_all(attrs={"class": "yt-uix-tile-link"})[1]['href']
        return "https://www.youtube.com" + res

    @staticmethod
    def rand_find(query):
        """
        Returns a random result of a youtube video for a topic
        :param query: topic
        :return: link/url to the video
        """
        query = urllib.parse.quote(query)
        url = "https://www.youtube.com/results?search_query=" + query
        respone = urllib.request.urlopen(url)
        html = respone.read()
        res = BeautifulSoup(html, 'html.parser').find_all(attrs={"class": "yt-uix-tile-link"})[random.randint(0, 20)][
            'href']
        return "https://www.youtube.com" + res
