#!/usr/bin/env python
# encoding: utf-8
"""
testrequesturl.py

Created by 李 瑞 on 2013-04-24.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import urllib2

class DownloadYouku():
    def __init__(self):
        global model, pv, nettype
        model = ['HTC One', 'HTC Hero', 'HTC Desire S', 'HTC Desire X', 'HTC Butterfly', 'HTC J', 'HTC ONE X', 'HTC T326H', 'HTC T328H', 'XIAOMI MI 1', 'XIAOMI MI 2', 'SAMSUNG Galaxy S', 'SAMSUNG galaxy SII', 'SAMSUNG GALAXY III', 'SAMSUNG NOTE', 'SAMSUNG NOTE2', 'SAMSUNG N8000', 'SAMSUNG i9200', 'SAMSUNG tab2', 'SAMSUNG tab']
        pv = ['2.1', '2.0', '2.2', '2.3', '2.0.1', '1.1']
        nettype = ['WIFI', '3G', 'CMNET', 'CMWAP']
        ver = ['4.1.2', '4.1.1', '4.0', '3.0', '3.0.1', '2.2.3', '2.3.1', '2.2', '2.3']
        self._model = model
        self._pv = pv
        self._nettype = nettype
        self._ver = ver
    
    def anzhuoshichang(self, nettype='WIFI', model='MI 2', mac='c4:6a:b7:4e:e3:36', device='867064014692428'):
        headers = {'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)'
        ,'Connection': 'Keep-Alive'
        ,'Host': 'market.hiapk.com'
        ,'channel': 'WAf+MfsjFao6DAlFVsg6eJZe7OqbUFxM'
        ,'partial': '0'
        ,'abi': 'armeabi-v7a|armeabi'
        ,'applang': '3'
        ,'authorizations': '0'
        ,'vender': '17001'
        ,'sdkversion': '16'
        ,'density': '320'
        ,'resolution': '720x1280'
        ,'nettype': nettype
        ,'model': model
        ,'mac': mac
        ,'device': device
        ,'pv': '2.2'
        ,'Accept-Encoding': 'gzip'
        ,'ts': '6'
        ,'sessionid': ''
        ,'clientmarket': '1'
        ,'peer': '1'}
    
        url = 'http://market.hiapk.com/service/api2.php?qt=9001&apk=1385361&sign=416b23f9fe509057bbebe8ef78dd12e9&lowapkmd5=null&type=1&source=26';
        req = urllib2.Request(url, '', headers)
        return req
        # try:
        #     response = urllib2.urlopen(req)
        # except HTTPError, e:
        #     print 'The server couldn\'t fulfill the request.'
        #     print 'anzhuoshichang() Error code: ', e.code
        # except URLError, e:
        #     print 'We failed to reach a server.'
        #     print 'anzhuoshichang() Reason: ', e.reason
        # else:
        #     # everything is fine
        #     the_page = response.read()
        #     print 'anzhuoshichang() response : ', the_page



    def anzhuo91(self, dm='MI+2', imei='867064014692428', imsi='460020666402074', placeid='222029981', mac='c4:6a:b7:4e:e3:36', device='867064014692428') :
        headers = {'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)'
        ,'Connection': 'Keep-Alive'
        ,'Host': 'market.hiapk.com'
        ,'channel': 'WAf+MfsjFao6DAlFVsg6eJZe7OqbUFxM'
        ,'partial': '0'
        ,'abi': 'armeabi-v7a|armeabi'
        ,'applang': '3'
        ,'authorizations': '0'
        ,'vender': '17001'
        ,'sdkversion': '16'
        ,'density': '320'
        ,'resolution': '720x1280'
        ,'nettype': 'WIFI'
        ,'model': 'MI 2'
        ,'mac': 'c4:6a:b7:4e:e3:36'
        ,'device': '867064014692428'
        ,'pv': '2.2'
        ,'Accept-Encoding': 'gzip'
        ,'ts': '6'
        ,'sessionid': ''
        ,'clientmarket': '1'
        ,'peer': '1'}
    
        url = 'http://bbxdata.sj.91.com/stat.ashx?mt=4&sv=3.2.9.5&osv=4.1&cpu=armeabi-v7a,armeabi&imei=%s&imsi=%s&nt=10&dm=%s&act=101&resid=4707975&stattype=4&restype=1&isincr=0&placeid=%s&' % (imei, imsi, dm, placeid)
        url = url.replace(' ', '+')
        #print url
        
        req = urllib2.Request(url)
        return req
        # try:
        #     response = urllib2.urlopen(req)
        # except HTTPError, e:
        #     print 'The server couldn\'t fulfill the request.'
        #     print 'anzhuo91() Error code: ', e.code
        # except URLError, e:
        #     print 'We failed to reach a server.'
        #     print 'anzhuo91() Reason: ', e.reason
        # else:
        #     # everything is fine
        #     the_page = response.read()
        #     print 'anzhuo91() response : ', the_page
    
    def shouji360_1(self) :
        
        url = 'http://s.360.cn/360baohe/index.php?para=QWN0aW9uPWFib3gmbWlkPWY1Mjk4NDk4ZTM2MTFhOTY3YjUxNjc3ZGEwYmRkMGEyJlVpVmVyc2lvbj0xMDAmTXlWZXJzaW9uPTEuOS41NSZDaGFubmVsPTYyMDAwMCZBbmRyb2lkSUQ9MmY4YWM2ZjAyZjA0MDM0ZSZOZXRUeXBlPTEmRGF0YT0lMzU4MV9seTMxX2tzMF9tYXJrZXQzNjBtYXJrZXRfemwxNCZhdD0xJmZyb209Y2F0aV9zZjAwNF9jc2lkMTRfMF8zJnN0YXJ0eXBlPTEmcnRpbWU9MTM2NzA0OTM4MzE2OSZzaWduPTk5MjI0MTA0QjM0REQyODM2OUQzRjMxNzY4REFERjBE'
        req = urllib2.Request(url)
        return req
    
    def shouji360_2(self) :

        url = 'http://s.360.cn/360baohe/index.php?para=QWN0aW9uPWFib3hpbnN0YWxsJm1pZD1mNTI5ODQ5OGUzNjExYTk2N2I1MTY3N2RhMGJkZDBhMiZVaVZlcnNpb249MTAwJk15VmVyc2lvbj0xLjkuNTUmQ2hhbm5lbD02MjAwMDAmQW5kcm9pZElEPTJmOGFjNmYwMmYwNDAzNGUmTmV0VHlwZT0xJm9zPTE2JmFwcGlkPTM1ODEmcG5hbWU9Y29tLnlvdWt1LnBob25lJnNpemU9NzM1MjE3MyZ2Y29kZT0zNCZ1cmw9aHR0cCUzQSUyRiUyRm0uc2hvdWppLjM2MHRwY2RuLmNvbSUyRjM2MHNqJTJGZGV2JTJGMjAxMzA0MjYlMkZjb20ueW91a3UucGhvbmVfMzRfMTcwMTI5LmFwayZpbnN0YWxsVHlwZT0xJnJlc3VsdFR5cGU9MCZmcm9tPWNhdGlfc2YwMDRfY3NpZDE0XzBfMyZzdGFydHlwZT0x'
        req = urllib2.Request(url)
        return req
    
    
    
    def baiduzhushou_1(self, uid='360F505CC708AB56E4F071B29BC48D65', pingpai='Xiaomi', xinghao='MI%%25', ver='4.1.1'):
        url = 'http://m.baidu.com/app?uid=%s%%257C824296410460768&f=content%%40&=&psize=3&usertype=0&ver=16780556&from=1092gs&tj=soft_2952022_1827869107_%%E4%%BC%%98%%E9%%85%%B7&operator=460020&network=WF&pkname=com.baidu.appsearch&country=CN&gms=true&platform_version_id=16&firstdoc=2692127&action=download&pu=cua%%40720_1280_android_4.0_320%%2Cosname%%40baiduappsearch%%2Cctv%%401%%2Ccfrom%%401092gs%%2Ccuid%%40%s%%25257C824296410460768%%2Ccut%%40%s_%s_16_%s&language=zh&apn=&' % (uid, uid, xinghao, ver, pingpai)
        req = urllib2.Request(url)
        return req
    
    def baiduzhushou_2(self, uid='360F505CC708AB56E4F071B29BC48D65', pingpai='Xiaomi', xinghao='MI%%25', ver='4.1.1'):
        url = 'http://m.baidu.com/app?uid=%s%%257C824296410460768&f=content%%40topupsoft%%4010%%401&=&psize=3&usertype=0&ver=16780556&from=1092gs&tj=soft_2952022_1827869107_%%E4%%BC%%98%%E9%%85%%B7&operator=460020&network=WF&pkname=com.baidu.appsearch&country=CN&gms=true&platform_version_id=16&firstdoc=2692127&action=download&pu=cua%%40720_1280_android_4.0_320%%2Cosname%%40baiduappsearch%%2Cctv%%401%%2Ccfrom%%401092gs%%2Ccuid%%40%s%%25257C824296410460768%%2Ccut%%40%s_%s_16_%s&language=zh&apn=&' % (uid, uid, xinghao, ver, pingpai)
        req = urllib2.Request(url)
        return req

def main():
	#anzhuoshichang();
	#anzhuo91();
	pass


if __name__ == '__main__':
	main()

