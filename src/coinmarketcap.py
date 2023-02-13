from src.helpers.driver_initializer import DriverInitializer
from src.helpers.coins import Coin
from src.helpers.file import File
import os
from src.helpers.logger import Logger
from src.helpers.config import Config


class CoinMarketCap:

    def __init__(self, coin_limit, start_page_no, headless, retry_limit=1):
        self.URL = "https://coinmarketcap.com/coins/?page={}".format(start_page_no)
        self.__driver = ""
        self.coin_limit = coin_limit
        self.coins = {}
        self.retry_limit = retry_limit
        self.headless = headless

    def __start_driver(self):
        self.__driver = DriverInitializer(self.headless).init()

    def __close_driver(self):
        self.__driver.close()
        self.__driver.quit()

    def __fetch_data(self):
        try:
            elements = Coin.element_list(self.__driver, self.coin_limit)
            if len(elements) > 0:
                for index, url in enumerate(elements, start=1):
                    self.__driver.get(url)
                    self.coins[index] = Coin.coin_data(self.__driver)
        except Exception as e:
            log = Logger()
            log.error(
                "Error in __fetch_data method : {}".format(e))

    def scrap(self):
        try:
            self.__start_driver()
            self.__driver.get(self.URL)
            self.__fetch_data()
            self.__close_driver()
            data = dict(list(self.coins.items())
                        [0:int(self.coin_limit)])
            return data
        except Exception as e:
            self.__close_driver()
            log = Logger()
            log.error(
                "Error in scrap method : {}".format(e))


def run(filename: str = "", directory: str = os.getcwd() + '/data'):
    config = Config()
    coin_limit = config.COIN_LIMIT
    start_page_no = config.START_PAGE_NO
    filename = config.DATA_FILE_NAME
    headless = config.HEADLESS
    retry_limit = config.RETRY_LIMIT
    data = CoinMarketCap(coin_limit, start_page_no, headless, retry_limit).scrap()
    File.write_csv(filename=filename, data=data, directory=directory)


if __name__ == '__main__':
    run()
