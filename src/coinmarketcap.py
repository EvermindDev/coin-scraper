from src.helpers.driver_initializer import DriverInitializer


class CoinMarketCap:

    def __init__(self, coins_count, headless):
        self.URL = "https://coinmarketcap.com"
        self.__driver = ""
        self.coins_count = coins_count
        self.retry = 3
        self.headless = headless

    def __start_driver(self):
        self.__driver = DriverInitializer(self.headless).init()

    def __close_driver(self):
        self.__driver.close()
        self.__driver.quit()

    def scrap(self):
        try:
            self.__start_driver()
            self.__driver.get(self.URL)
            self.__close_driver()
            return None
        except Exception as ex:
            self.__close_driver()


def run():
    CoinMarketCap(2, False).scrap()


if __name__ == '__main__':
    run()
