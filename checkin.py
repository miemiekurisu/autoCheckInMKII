#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import cookielib
import urllib
from ConfigParser import SafeConfigParser
import logging
import logging.handlers
import aspect



#主签到程序
@aspect.timeit
def checkIn(loginurl, checkurl,user,password):  
    try:  
        #保存cookie
        cj = cookielib.CookieJar()  
        #cookieJar作为参数，获得一个opener的实例  
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
        #伪装成IE
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]  
        #生成Post数据，含有登陆用户名密码。  
        data = urllib.urlencode({"user":user,"password":password})  
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie  
        opener.open(loginurl,data)  
        #以带cookie的方式访问页面  
        op=opener.open(checkurl)  
        #读取页面源码  
        data= op.read()
        return data
    except Exception,e:  
        print str(e) 
        

def main():
    cfg = SafeConfigParser()
    cfg.read('checkinfo.cfg')
    loginurl=cfg.get('urlinfo','loginurl')
    checkurl=cfg.get('urlinfo','checkurl')
    user=cfg.get('userinfo','username')
    password=cfg.get('userinfo','password')
    data = checkIn(loginurl, checkurl,user,password)
    
if __name__ == '__main__':
    main()