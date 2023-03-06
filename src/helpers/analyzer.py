import csv
import os
import numpy as np
from rich.console import Console
from src.helpers.wrapper import Wrapper


def load_data_from_file(data_file, limit):
    data = np.genfromtxt(data_file, delimiter=",", skip_header=1, max_rows=limit)
    return data


def filter_data(data):
    market_cap = data[:, -1]
    median_cap = np.median(market_cap)
    market_cap_filter = market_cap > median_cap

    filtered_data = data[market_cap_filter, :]
    return filtered_data


def calculate_data(data, num_days):
    date, open_price, high, low, close_price, volume, market_cap = np.split(
        data, 7, axis=1
    )

    # Calculate percentage change in all days' price
    first_close = close_price[-1]
    last_close = close_price[0]
    pct_change = ((last_close - first_close) / first_close) * 100

    # Calculate the 90th percentile of the high prices
    high_percentile = np.percentile(high, 90)

    # Calculate the lowest and highest prices in the last n days
    last_n_days = data[-num_days:]
    lowest_price = np.min(last_n_days[:, 3])
    highest_price = np.max(last_n_days[:, 2])

    row = {
        "mean_closing_price": "{:.2f}".format(np.mean(close_price)),
        "standard_deviation_high_prices": "{:.4f}".format(np.std(high)),
        "minimum_volume": "{:.0f}".format(np.min(volume)),
        "maximum_market_cap": "{:.0f}".format(np.max(market_cap)),
        "high_percentile": "{:.2f}".format(high_percentile),
        "price_change": "{:.2f}%".format(pct_change[0]),
        "lowest_price_last_n_days": "{:.2f}".format(lowest_price),
        "highest_price_last_n_days": "{:.2f}".format(highest_price),
    }

    return row


class Analyzer:
    def __init__(self, config):
        self.config = config

    def execute(self):
        main_file = os.path.join(
            self.config.DATA_DIRECTORY,
            f"{self.config.DATA_FILE_NAME}.{self.config.DATA_FILE_FORMAT}",
        )

        if os.path.exists(main_file):
            data_rows = self.read_csv(main_file)
            wrapper = Wrapper()
            table = wrapper.create_table(data_rows, self.config.HISTORICAL_TIME_RANGE, self.config.CURRENCY_SYMBOL)
            console = Console()
            console.print(table)
        else:
            print(f"The file '{main_file}' does not exist. Please scrape data first")

    def read_csv(self, file_path):
        data_rows = []
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                name, slug, symbol, rank, watchlist, logo, entry_datetime = row
                analyzer_data = self.calc_data(slug)
                row_historical = {
                    "rank": rank,
                    "name": name,
                    "symbol": symbol,
                    "logo": logo,
                    "mean_closing_price": analyzer_data["mean_closing_price"],
                    "standard_deviation_high_prices": analyzer_data[
                        "standard_deviation_high_prices"
                    ],
                    "minimum_volume": str(analyzer_data["minimum_volume"]),
                    "maximum_market_cap": str(analyzer_data["maximum_market_cap"]),
                    "high_percentile": str(analyzer_data["high_percentile"]),
                    "price_change": str(analyzer_data["price_change"]),
                    "watchlist": watchlist,
                    "lowest_price_last_n_days": str(analyzer_data["lowest_price_last_n_days"]),
                    "highest_price_last_n_days": str(analyzer_data["highest_price_last_n_days"]),
                }
                data_rows.append(row_historical)
        return data_rows

    def calc_data(self, slug):
        data_file = os.path.join(
            self.config.DATA_DIRECTORY + "/historical",
            f"{slug}.{self.config.DATA_FILE_FORMAT}",
        )

        if not os.path.exists(data_file):
            print(f"The file '{slug}' does not exist.")
            return {}

        data = load_data_from_file(data_file, self.config.HISTORICAL_TIME_RANGE)
        filtered_data = filter_data(data)
        calculated_data = calculate_data(filtered_data, self.config.HISTORICAL_TIME_RANGE)

        return calculated_data

