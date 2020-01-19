import praw, random
from classified.globals import *


class RedditBot:
    def __init__(self):
        """
        Logs to reddit with praw.
        """
        self.r = praw.Reddit(client_id=reddit_class_client_id, client_secret=reddit_class_client_secret,
                             username=reddit_class_username,
                             password=reddit_class_password, user_agent=reddit_class_user_agent)

    def top_post_subreddit(self, sub_reddit: str):
        """
        Returns the top post from a certain subreddit
        :param sub_reddit: subreddit to search from
        :return: post rating of age, post url
        """
        subreddit = self.r.subreddit(sub_reddit)
        posts = subreddit.hot(limit=10)
        for i, post in enumerate(posts):
            if not post.stickied:  # Ignore stickied posts since they're 95% of the time not content
                return post.over_18, post.url

    def random_post_sub(self, sub: str):
        """
        Returns a random post from a subreddit
        :param sub: subreddit to look from
        :return: post age rating, post url
        """
        try:
            #   Use the reddit random button from a asubreddit
            post = self.r.subreddit(sub).random()
            return post.over_18, post.url
            #   Some don't have this button, so we make our own random!
        except Exception:
            posts = self.r.subreddit(sub).hot(limit=100)
            post_nr = random.randint(0, 100)
            for i, postt in enumerate(posts):
                if i == post_nr:
                    return postt.over_18, postt.url

    def search_first_topic(self, topic: str):
        """
        Returns the first post for a topic from reddit
        :param topic: thing to look for
        :return: post age rating, post url
        """
        all = self.r.subreddit("all")
        for i in all.search(topic, limit=5):
            return i.over_18, i.url

    def search_topic_random(self, topic: str):
        """
        Returns a random result from reddit for a topic
        :param topic: thing to look for
        :return: post age rating, post url
        """
        all = self.r.subreddit("all")
        rand_nr = random.randint(1, 99)
        results = all.search(topic, limit=100)
        list_of_results = list(results)
        if len(list_of_results) == 0:
            return 0, "No results found"
        choice = random.choice(list_of_results)
        return choice.over_18, choice.url

    def top_x_posts(self, sub: str, n: int):
        """
        Returns the first N posts from a certain subreddit
        :param n: integer value, representing number of posts.
        :param sub: the subreddit, string
        :return: TODO
        """
        if n > 500:
            return -1, -1
        posts = self.r.subreddit(sub).hot(limit=10)
        url_list = []
        over_18 = False

        for i, postt in enumerate(posts):
            if n == 0:
                return over_18, "\n".join(url_list)
            if not postt.stickied:
                url_list.append(postt.url)
                n -= 1
            if postt.over_18:
                over_18 = True
        return over_18, "\n".join(url_list)
