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
            name = driver.find_element(By.XPATH, '//h2/span/span').text
            symbol = driver.find_element(By.XPATH, '//h2/small[@class="nameSymbol"]').text

            rank_data = driver.find_element(By.XPATH, '//div[@class="namePill namePillPrimary"]').text
            rank_match = re.search(r"#\d+", rank_data)
            if rank_match:
                rank_number = int(re.sub(r"#", "", rank_match.group()))
            else:
                rank_number = ''

            watchlist_data = driver.find_element(By.XPATH, '//div[contains(text(), "watchlists")]').text
            watchlist_count = ''
            if watchlist_data:
                watchlist_match = re.search(r"^On\s*(\d{1,3}(?:,\d{3})*)\s*watchlists$", watchlist_data)
                if watchlist_match:
                    watchlist_count = int(re.sub(",", "", watchlist_match.group(1)))

            logo = driver.find_element(By.XPATH, '//div[contains(@class, "nameHeader")]/img')
            logo_img_url = logo.get_attribute('src')

            return {
                "name": name,
                "symbol": symbol,
                "rank": rank_number,
                "watchlist": watchlist_count,
                "logo": logo_img_url
            }

        except Exception as e:
            log = Logger()
            log.error(
                "Error in coin_data method : {}".format(e))
            return {}
