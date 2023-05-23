import logging #стандартна бібліотека для логування перебігу програми
logging.basicConfig(level = logging.DEBUG , format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug("debug") #показує стандартний перебіг програми
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")
