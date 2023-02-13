import configparser

CONFIG_FILE_NAME = "config.cfg"
COINBASECAP_CONFIG_SECTION = "coinbasecap"
SCRAP_CONFIG_SECTION = "scrap"
DATA_CONFIG_SECTION = "data"
LOGS_CONFIG_SECTION = "logs"


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_NAME)

        self.COIN_LIMIT = int(config.get(COINBASECAP_CONFIG_SECTION, "coin_limit"))
        self.START_PAGE_NO = int(config.get(COINBASECAP_CONFIG_SECTION, "start_page_no"))

        self.HEADLESS = eval(config.get(SCRAP_CONFIG_SECTION, "headless"))
        self.RETRY_LIMIT = int(config.get(SCRAP_CONFIG_SECTION, "retry_limit"))

        self.DATA_FILE_NAME = config.get(DATA_CONFIG_SECTION, "data_file_name")
        self.DATA_FILE_FORMAT = config.get(DATA_CONFIG_SECTION, "data_file_format")

        self.LOG_FILE_NAME = config.get(LOGS_CONFIG_SECTION, "log_file_name")


