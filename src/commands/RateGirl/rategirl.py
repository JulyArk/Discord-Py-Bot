import datetime


class RateGirl:
    def rategirl(self, user_id: float):
        """
        Using pseudo RNG, generate 2 numbers between 0-10 (float)
        The RNG formula is based on day and month as well as the user ID given
        :param user_id: float
        :return: Hot(Float) , Crazy (Float)
        """
        today = datetime.date.today().day
        month = datetime.date.today().month
        # hot = float(user_id % ((((today % month) * (today * month)) % 1000) / 100))
        # generate hot value
        #   RNG formula
        hot = float(user_id % ((2 * today + 2 * month + month * today) * month * today) / (
                user_id % (month * today + today % month))) % 9.9995
        hot = float("{0:.2f}".format(hot))  # format to 2 decimals
        # generate crazy value
        #   RNG formula
        crazy = float(user_id % ((5 * today + 3 * month + month * today) * month * today) / (
                user_id % (month * today + 2 * today % month))) % 9.9995
        crazy = float("{0:.2f}".format(crazy))  # format to 2 decimals
        return hot, crazy
