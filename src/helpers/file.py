import os
import csv


class File:
    @staticmethod
    def write_csv(filename, data, directory):
        os.chdir(directory)
        fieldnames = ['name', 'symbol']
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
                    "symbol": data[key]['symbol']
                }
                writer.writerow(row)
            data_file.close()
