import os
import time
import datetime

from src.helpers.config import Config
from src.helpers.driver_initializer import DriverInitializer
from src.helpers.file import File
from src.helpers.logger import Logger
from src.helpers.coins import Coin


class CoinMarketCap:

    def __init__(self, config):
        self.URL = f"https://coinmarketcap.com/coins/?page={config.START_PAGE_NO}"
        self.config = config
        self.driver = DriverInitializer(config.HEADLESS).init()
        self.coins = {}
        self.entry_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def fetch_data(self):
        try:
            elements = Coin.element_list(self.driver, self.config.COIN_LIMIT)
            for index, url in enumerate(elements, start=1):
                self.driver.get(url)
                self.coins[index] = Coin.coin_data(self.driver, self.entry_datetime, self.config.DATA_DOWNLOAD_LOGO)
                time.sleep(1)
        except Exception as e:
            Logger().error("Error in fetch_data method : {}".format(e))

    def scrap(self):
        try:
            self.driver.get(self.URL)
            self.fetch_data()
        except Exception as e:
            Logger().error("Error in scrap method : {}".format(e))
        finally:
            self.driver.close()
            self.driver.quit()

        data = dict(list(self.coins.items())[0:int(self.config.COIN_LIMIT)])
        return data


def run(directory: str = os.getcwd() + '/data'):
    config = Config()
    data = CoinMarketCap(config).scrap()
    File.write_csv(filename=config.DATA_FILE_NAME, data=data, directory=directory)


if __name__ == '__main__':
    run()
