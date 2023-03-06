from selenium.webdriver.common.by import By
import re

from src.helpers.logger import Logger
from src.helpers.file import File
from src.helpers.helper import Helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
from src.helpers.config import Config


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
    def coin_data(driver, entry_datetime, config):
        try:
            name = driver.find_element(By.XPATH, '//h2/span/span').text
            symbol = driver.find_element(By.XPATH, '//h2/small[@class="nameSymbol"]').text
            slug = Helper.slugify(name)

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

            logo_file_name = ''

            if config.DATA_DOWNLOAD_LOGO:
                logo = driver.find_element(By.XPATH, '//div[contains(@class, "nameHeader")]/img')
                logo_img_url = logo.get_attribute('src')
                file = File()
                logo_file_name = symbol.lower() + '.png'
                file.download_image(logo_file_name, logo_img_url, 'data/logo')

            if config.ENABLE_HISTORICAL_DATA:
                Coin.coin_historical_data(driver, slug, config)

            return {
                "name": name,
                "slug": slug,
                "symbol": symbol,
                "rank": rank_number,
                "watchlist": watchlist_count,
                "logo": logo_file_name,
                'entry_datetime': entry_datetime
            }

        except Exception as e:
            log = Logger()
            log.error(
                "Error in coin_data method : {}".format(e))
            return {}

    @staticmethod
    def coin_historical_data(driver, coin, config):
        if config.HISTORICAL_TIME_RANGE > 0:
            try:
                wait = WebDriverWait(driver, 10)
                # Wait for the link to become clickable
                historical_data_link = wait.until(
                    EC.element_to_be_clickable((By.XPATH, f"//a[@href='/currencies/{coin}/historical-data/']"))
                )
                historical_data_link.click()

                # Wait until the table is available
                table = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='history']//table")))

                # Extract data from the table
                headers = [header.text for header in table.find_elements(By.XPATH, ".//thead/tr")]
                rows = []
                for i, row in enumerate(table.find_elements(By.XPATH, ".//tbody/tr")):
                    if i >= config.HISTORICAL_TIME_RANGE:
                        break
                    row_data = [data.text for data in row.find_elements(By.XPATH, ".//td")]
                    row_historical = {
                        "date": datetime.strptime(row_data[0], '%b %d, %Y').strftime('%Y-%m-%d'),
                        "open": Helper.normalize_price(row_data[1]),
                        "high": Helper.normalize_price(row_data[2]),
                        "low": Helper.normalize_price(row_data[3]),
                        "close": Helper.normalize_price(row_data[4]),
                        "volume": Helper.normalize_price(row_data[5]),
                        "market_cap": Helper.normalize_price(row_data[6]),
                    }
                    rows.append(row_historical)

                File.write_historical_csv(filename=coin, data=rows, directory=config.DATA_DIRECTORY)

            except Exception as e:
                log = Logger()
                log.error(
                    "Error in coin_historical_data method : {}".format(e))
                return {}

        return
