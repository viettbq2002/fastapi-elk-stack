import logging
import time
import yaml
class LoggerSetup:
    def __init__(self) -> None:
        self.logger = logging.getLogger("")
        self.setup_logging()
    def setup_logging(self):
        with open("app/log_conf.yaml") as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
            self.logger.info("Logging configured")
