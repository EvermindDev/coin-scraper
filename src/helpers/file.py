import os
import csv
from src.helpers.logger import Logger


class File:

    @staticmethod
    def write_csv(filename, data, directory):
        log = Logger()
        os.chdir(directory)
        fieldnames = ['name', 'symbol', 'rank', 'watchlist', 'logo']
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
                    "logo": data[key]['logo']
                }
                writer.writerow(row)
            data_file.close()
        log.info('Data successfully saved in file {}.csv'.format(filename))
