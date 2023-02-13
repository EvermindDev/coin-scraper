import os
import csv
from src.helpers.logger import Logger
import urllib.request
from src.helpers.logger import Logger


class File:

    @staticmethod
    def write_csv(filename, data, directory):
        log = Logger()
        os.chdir(directory)
        fieldnames = ['name', 'symbol', 'rank', 'watchlist', 'logo', 'entry_datetime']
        mode = 'w'
        if os.path.exists("{}.csv".format(filename)):
            mode = 'a'
        with open("{}.csv".format(filename), mode, newline='', encoding="utf-8") as data_file:
            writer = csv.DictWriter(data_file, fieldnames=fieldnames)
            if mode == 'w':
                writer.writeheader()
            for key in data:
                row = {
                    "name": data[key]['name'],
                    "symbol": data[key]['symbol'],
                    "rank": data[key]['rank'],
                    "watchlist": data[key]['watchlist'],
                    "logo": data[key]['logo'],
                    "entry_datetime": data[key]['entry_datetime']
                }
                writer.writerow(row)
            data_file.close()
        log.info('Data successfully saved in file {}.csv'.format(filename))

    @staticmethod
    def download_image(filename, src, directory):
        try:
            image_path = os.path.abspath(os.path.join(os.getcwd(), directory, filename))
            urllib.request.urlretrieve(src, image_path)
        except Exception as e:
            log = Logger()
            log.error(
                "An error occurred while downloading the image : {}".format(e))
