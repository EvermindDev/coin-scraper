from selenium.webdriver.common.by import By
import re
from src.helpers.logger import Logger


class Coin:
    @staticmethod
    def element_list(driver, limit) -> list:
        regex_coin = r'(\/)currencies\/*\/[a-z-]*\/$'
        pattern = re.compile(regex_coin)
        list_of_urls = []
        try:
            elements = driver.find_elements(By.XPATH, '//a[@class="cmc-link"]')
            for link in elements:
                href = link.get_attribute('href')
                if pattern.search(href):
                    list_of_urls.append(href)
                else:
                    pass

                if len(list_of_urls) >= limit:
                    break
            return list_of_urls
        except Exception as e:
            log = Logger()
            log.error(
                "Error in element_list method : {}".format(e))
            return []

    @staticmethod
    def coin_data(driver):
        try:
            name = driver.find_element(By.XPATH, '//h2/span/span')
            symbol = driver.find_element(By.XPATH, '//h2/small[@class="nameSymbol"]')

            return {
                "name": name.text,
                "symbol": symbol.text
            }

        except Exception as e:
            log = Logger()
            log.error(
                "Error in coin_data method : {}".format(e))
            return {}
