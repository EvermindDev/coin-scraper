import logging.handlers


class Logger:
    Logger = None

    def __init__(self, log="main"):
        self.Logger = logging.getLogger(f"{log}_logger")
        self.Logger.setLevel(logging.DEBUG)
        self.Logger.propagate = False
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        log_fn = logging.FileHandler(f"logs/{log}.log")
        log_fn.setLevel(logging.DEBUG)
        log_fn.setFormatter(formatter)
        self.Logger.addHandler(log_fn)

    def log(self, message, level="info"):
        if level == "info":
            self.Logger.info(message)
        elif level == "warning":
            self.Logger.warning(message)
        elif level == "error":
            self.Logger.error(message)
        elif level == "debug":
            self.Logger.debug(message)

    def info(self, message):
        self.log(message, "info")

    def warning(self, message):
        self.log(message, "warning")

    def error(self, message):
        self.log(message, "error")

    def debug(self, message):
        self.log(message, "debug")
