import logging
class LoggingBase():   

    LOGNAME=None
    LOGFORMAT=None
    LOG2FILE=False
    LOG2CONSOLE=False

    def makeLogger(self):
        self.logger = logging.getLogger(self.LOGNAME)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(self.LOGFORMAT)
        if self.LOG2FILE:
            fh =logging.FileHandler(f'{self.LOGNAME}.log')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        if self.LOG2CONSOLE:    
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
        return self.logger
    
    def log(self,message,level="info"):
        if not hasattr(self.logger,level):
            raise AttributeError("level not found on logger")
        _logger = getattr(self.logger,level)
        text = "{} - {}".format(type(self).__name__,str(message))
        return _logger(text)
    