from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as CustomChromeOptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverInitializer:
    def __init__(self, headless: bool):
        self.headless = headless

    def set_properties(self, options):
        if self.headless:
            options.add_argument("--headless")
        else:
            options.add_argument("--start-maximized")

        return options

    def set_driver(self):
        options = CustomChromeOptions()
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                options=self.set_properties(options))

    def init(self):
        driver = self.set_driver()
        return driver
