import logging

logging.basicConfig(filename="C://composer//SelniumLoging//test.log",                       #side slash important     level=logging.DEBUG)    this command will show all level of debug
                    format='%(asctime)s: %(levelname)s: %(message)s:',
                    level=logging.DEBUG
                   )
logging.debug("this is a debug message")
logging.warning("this is a debug message")

