import logging
import os.path
import time
class Logger(object):
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        fh = logging.FileHandler("./logs")
        rq=time.strftime('%Y%m%d%H',time.localtime(time.time()))

        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'

        log_name=log_path+rq+'.log'
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
    def getlog(self):
        return self.logger
