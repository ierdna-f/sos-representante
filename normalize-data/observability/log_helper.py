import logging

class Log:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger("InventoryApp")

    @staticmethod
    def info(message):
        Log.logger.info(f"[INFO] {message}")

    @staticmethod
    def error(message):
        Log.logger.error(f"[ERROR] {message}")

    @staticmethod
    def debug(message):
        Log.logger.debug(f"[DEBUG] {message}")