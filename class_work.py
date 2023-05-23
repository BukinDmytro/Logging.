import logging #стандартна бібліотека для логування перебігу програми
logging.basicConfig(level = logging.DEBUG ,
                    filename = "logs.log" ,
                    filemode = "w" ,
                    format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug("debug") #показує стандартний перебіг програми
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")

try:
    print(10/0)
except Exception:
    logging.exception("Fignya")

