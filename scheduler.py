#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import cookielib
import urllib
from ConfigParser import SafeConfigParser
import aspect
from apscheduler.schedulers.background import BackgroundScheduler
import checkin
import os
import time

def maincheck():
    cfg = SafeConfigParser()
    cfg.read('checkinfo.cfg')
    loginurl=cfg.get('urlinfo','loginurl')
    checkurl=cfg.get('urlinfo','checkurl')
    user=cfg.get('userinfo','username')
    password=cfg.get('userinfo','password')
    print 'start'
    data = checkin.checkIn(loginurl, checkurl,user,password)
    print data
    print 'End Check'


def heart():
    pass

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