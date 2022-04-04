import logging
import time

class Log:

    def __init__(self,logger, file_level):

        self.logger=logging.getLogger(logger)

        current_time=time.strftime("%Y-%m-%d-%H-%M")
        log_name="C:\\Users\\AZ\\POM_project\\logs\\loger"+current_time+".log"
        filehandler=logging.FileHandler(log_name,mode="w")
        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        self.logger.addHandler(filehandler)
        self.logger.setLevel(file_level)


