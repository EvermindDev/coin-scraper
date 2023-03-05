import configparser

CONFIG_FILE_NAME = "config.cfg"
COINBASECAP_CONFIG_SECTION = "coinbasecap"
SCRAPE_CONFIG_SECTION = "scrape"
DB_CONFIG_SECTION = "db-data"
DATA_CONFIG_SECTION = "file-data"
LOGS_CONFIG_SECTION = "logs"


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_NAME)

        self.COIN_LIMIT = int(config.get(COINBASECAP_CONFIG_SECTION, "coin_limit"))
        self.START_PAGE_NO = int(config.get(COINBASECAP_CONFIG_SECTION, "start_page_no"))

        self.HEADLESS = eval(config.get(SCRAPE_CONFIG_SECTION, "headless"))
        self.RETRY_LIMIT = int(config.get(SCRAPE_CONFIG_SECTION, "retry_limit"))

        self.DATA_DB_USE = eval(config.get(DB_CONFIG_SECTION, "use_database"))
        self.DATA_DB_HOST = config.get(DB_CONFIG_SECTION, "host")
        self.DATA_DB_USER = config.get(DB_CONFIG_SECTION, "user")
        self.DATA_DB_PASSWORD = config.get(DB_CONFIG_SECTION, "password")
        self.DATA_DB_DATABASE = config.get(DB_CONFIG_SECTION, "database")

        self.DATA_FILE_USE = eval(config.get(DATA_CONFIG_SECTION, "use_file"))
        self.DATA_FILE_NAME = config.get(DATA_CONFIG_SECTION, "data_file_name")
        self.DATA_FILE_FORMAT = config.get(DATA_CONFIG_SECTION, "data_file_format")
        self.DATA_DOWNLOAD_LOGO = eval(config.get(DATA_CONFIG_SECTION, "download_logo"))

        self.LOG_FILE_NAME = config.get(LOGS_CONFIG_SECTION, "log_file_name")


