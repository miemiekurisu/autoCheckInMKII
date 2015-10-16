#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import cookielib
import urllib
from ConfigParser import SafeConfigParser
import logging
import logging.handlers
import aspect
from apscheduler.schedulers.background import BackgroundScheduler
import checkin
import os
import time
 

LOG_FILE = 'checkin.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) 
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)   
handler.setFormatter(formatter)      
logger = logging.getLogger('checkin')   
logger.addHandler(handler)          
logger.setLevel(logging.INFO)

@aspect.timeit
def maincheck():
    cfg = SafeConfigParser()
    cfg.read('checkinfo.cfg')
    loginurl=cfg.get('urlinfo','loginurl')
    checkurl=cfg.get('urlinfo','checkurl')
    user=cfg.get('userinfo','username')
    password=cfg.get('userinfo','password')
    logger.info('Start Check')   
    data = checkIn(loginurl, checkurl,user,password)
    logger.info('End Check')

def heart():
    logger.info('Live')

if __name__ == '__main__':
    cfg = SafeConfigParser()
    cfg.read('checkinfo.cfg')
    scheduler = BackgroundScheduler()
    CHECKDAY=cfg.get('cronexp','CHECKDAY')
    CHECKINHOUR=cfg.get('cronexp','CHECKINHOUR')
    CHECKINMINUTE=cfg.get('cronexp','CHECKINMINUTE')
    scheduler.add_job(maincheck,trigger='cron',day_of_week=CHECKDAY,hour=CHECKINHOUR,minute=CHECKINMINUTE,misfire_grace_time=60*60)
    scheduler.start()
    print('Please Press Ctrl+{0} to exit'.format('C' if os.name=='nt' else 'C'))

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt,SystemExit):
        scheduler.shutdown()