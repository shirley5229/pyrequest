# coding=utf-8
import os,sys
import time
import logbook
from logbook import Logger,StreamHandler,FileHandler
from logbook.more import ColorizedStderrHandler
from public import function

def setLog():
    logname=function.get_filepath("/logs/")+time.strftime('%Y-%m-%d') + '.log'
    StreamHandler(sys.stdout).push_application()
    FileHandler(logname, bubble=True).push_application()
    log = Logger("")
    return log


if __name__ == '__main__':
    log=setLog()
    log.info('info msg1000013333')
    log.debug('debug msg')
    log.warning('warning msg')
    log.error('error msg')
