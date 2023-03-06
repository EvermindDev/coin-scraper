import configparser
import os

CONFIG_FILE_NAME = "config.cfg"
ANALYZER_CONFIG_SECTION = "analyzer"
COINBASECAP_CONFIG_SECTION = "coinbasecap"
HISTORICAL_DATA_CONFIG_SECTION = "historical-data"
SCRAPE_CONFIG_SECTION = "scrape"
DB_CONFIG_SECTION = "db-data"
DATA_CONFIG_SECTION = "file-data"
LOGS_CONFIG_SECTION = "logs"


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_NAME)
        data_directory = config.get(DATA_CONFIG_SECTION, "data_directory")

        if data_directory:
            data_directory_path = os.getcwd() + '/' + eval(data_directory)
        else:
            data_directory_path = os.getcwd() + '/data'

        self.ANALYZER_MODE = eval(config.get(ANALYZER_CONFIG_SECTION, "mode"))

        self.COIN_LIMIT = int(config.get(COINBASECAP_CONFIG_SECTION, "coin_limit"))
        self.START_PAGE_NO = int(config.get(COINBASECAP_CONFIG_SECTION, "start_page_no"))
        self.CURRENCY = eval(config.get(COINBASECAP_CONFIG_SECTION, "currency"))
        self.CURRENCY_SYMBOL = eval(config.get(COINBASECAP_CONFIG_SECTION, "currency_symbol"))

        self.ENABLE_HISTORICAL_DATA = eval(config.get(HISTORICAL_DATA_CONFIG_SECTION, "enable_historical_data"))
        self.HISTORICAL_TIME_RANGE = eval(config.get(HISTORICAL_DATA_CONFIG_SECTION, "historical_time_range"))

        self.HEADLESS = eval(config.get(SCRAPE_CONFIG_SECTION, "headless"))
        self.TIME_SLEEP = int(config.get(SCRAPE_CONFIG_SECTION, "time_sleep"))
        self.RETRY_LIMIT = int(config.get(SCRAPE_CONFIG_SECTION, "retry_limit"))

        self.DATA_DB_USE = eval(config.get(DB_CONFIG_SECTION, "use_database"))
        self.DATA_DB_HOST = config.get(DB_CONFIG_SECTION, "host")
        self.DATA_DB_USER = config.get(DB_CONFIG_SECTION, "user")
        self.DATA_DB_PASSWORD = config.get(DB_CONFIG_SECTION, "password")
        self.DATA_DB_DATABASE = config.get(DB_CONFIG_SECTION, "database")

        self.DATA_FILE_USE = eval(config.get(DATA_CONFIG_SECTION, "use_file"))
        self.DATA_FILE_NAME = config.get(DATA_CONFIG_SECTION, "data_file_name")
        self.DATA_FILE_FORMAT = config.get(DATA_CONFIG_SECTION, "data_file_format")
        self.DATA_DIRECTORY = data_directory_path
        self.DATA_DOWNLOAD_LOGO = eval(config.get(DATA_CONFIG_SECTION, "download_logo"))

        self.LOG_FILE_NAME = config.get(LOGS_CONFIG_SECTION, "log_file_name")


