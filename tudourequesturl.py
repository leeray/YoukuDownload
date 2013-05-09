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

class DownloadTudou():
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
    
        url = 'http://market.hiapk.com/service/api2.php?qt=9001&apk=1432169&sign=c12d98ec7475ac3f0db8be0898bdc04b&lowapkmd5=null&type=1&source=26';
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



    def anzhuo91_1(self, dm='MI+2', imei='867064014692428', imsi='460020666402074', placeid='222029981', mac='c4:6a:b7:4e:e3:36', device='867064014692428') :
        
        url = 'http://bbx2.sj.91.com/softs.ashx?act=207&resid=4796706&resname=%%e5%%9c%%9f%%e8%%b1%%86%%e7%%94%%b5%%e5%%bd%%b1%%e7%%94%%b5%%e8%%a7%%86%%e5%%89%%a7&versionname=3.1&icon=http%%3a%%2f%%2fhiapk.91rb.com%%2fdata%%2fupload%%2f2013%%2f05_02%%2f16%%2f201305021616527543.png&catename=%%e8%%a7%%86%%e9%%a2%%91%%e8%%bd%%af%%e4%%bb%%b6&size=7.38MB&fsize=7743381&identifer=com.tudou.android&restype=1&versioncode=18&score=0&placeid=%s&mt=4&sv=3.2.9.5&pid=2&price=0.00&keyword=%%e5%%9c%%9f%%e8%%b1%%86&pos=250101&osv=4.1&cpu=armeabi-v7a,armeabi&imei=%s&nt=10&dm=GT-I9128V&iv=4&imsi=' % (placeid, imei)
        
        req = urllib2.Request(url)
        return req
        
    def anzhuo91_2(self, dm='MI+2', imei='867064014692428', imsi='460020666402074', placeid='222029981', mac='c4:6a:b7:4e:e3:36', device='867064014692428') :
        
        url = 'http://bbxdata.sj.91.com/stat.ashx?mt=4&sv=3.2.9.5&osv=4.1&cpu=armeabi-v7a,armeabi&imei=%s&nt=10&dm=GT-I9128V&act=101&resid=4796706&stattype=4&restype=1&isincr=0&placeid=%s&sign=lGkOm3rH4J92Hf1vHOLkijmLzvOE9uccXzE37fToJQ3qzMQ2jH7ELA%%3D%%3D&imsi=' % (imei, placeid)
        req = urllib2.Request(url)
        return req
    
    def anzhuo91_3(self, dm='MI+2', imei='867064014692428', imsi='460020666402074', placeid='222029981', mac='c4:6a:b7:4e:e3:36', device='867064014692428') :    
        url = 'http://sj.91rb.com/android/soft//2013/2/20/74b19a07223947e39fbcd44cfa863d62/com.tudou.android_18_3.1_635035419050632500.apk'
        req = urllib2.Request(url)
        return req
    
    def anzhuo91_4(self, dm='MI+2', imei='867064014692428', imsi='460020666402074', placeid='222029981', mac='c4:6a:b7:4e:e3:36', device='867064014692428') :   
        url = 'http://bbxdata.sj.91.com/stat.ashx?mt=4&sv=3.2.9.5&osv=4.1&cpu=armeabi-v7a,armeabi&imei=%s&nt=10&dm=GT-I9128V&act=101&resid=4796706&stattype=5&restype=1&root=0&isincr=0&placeid=%s&sign=lGkOm3rH4J92Hf1vHOLkijmLzvOE9uccXzE37fToJQ3P%%2FcwvHJ%%2FN1A%%3D%%3D&imsi=' % (imei, placeid)
        
        req = urllib2.Request(url)
        return req

    
    def shouji360_1(self) :
        
        url = 'http://s.360.cn/360baohe/index.php?para=QWN0aW9uPWFib3gmbWlkPWQ2ZWQxMjYzMTI5YWMwNmM2YjIxMTAyNzYzZGU3OTMxJlVpVmVyc2lvbj0xMDAmTXlWZXJzaW9uPTEuOS41NSZDaGFubmVsPTYyMDAwMCZBbmRyb2lkSUQ9N2I5MzU4ZDVlZDMwZGI5ZCZOZXRUeXBlPTEmRGF0YT0lNDEwN19seTMxX2tzMF9tYXJrZXQzNjBtYXJrZXRfemwxNCZhdD0xJmZyb209aG9tZV9zZjAwNF9jc2lkMTRfMF8zJnN0YXJ0eXBlPTEmcnRpbWU9MTM2ODA4MjczMzI4MCZzaWduPUQ5MTE3RDE4QjNGNTY0NUM0OEU0NzgwQjlEQjJFNDI4'
        req = urllib2.Request(url)
        return req
    
    def shouji360_2(self) :

        url = 'http://s.360.cn/360baohe/index.php?para=QWN0aW9uPWFib3hpbnN0YWxsJm1pZD1kNmVkMTI2MzEyOWFjMDZjNmIyMTEwMjc2M2RlNzkzMSZVaVZlcnNpb249MTAwJk15VmVyc2lvbj0xLjkuNTUmQ2hhbm5lbD02MjAwMDAmQW5kcm9pZElEPTdiOTM1OGQ1ZWQzMGRiOWQmTmV0VHlwZT0xJm9zPTE2JmFwcGlkPTQxMDcmcG5hbWU9Y29tLnR1ZG91LmFuZHJvaWQmc2l6ZT03NzU1NzA5JnZjb2RlPTE4JnVybD1odHRwJTNBJTJGJTJGbS5zaG91amkuMzYwdHBjZG4uY29tJTJGMzYwc2olMkZkZXYlMkYyMDEzMDQyOCUyRmNvbS50dWRvdS5hbmRyb2lkXzE4XzIxMzAyMi5hcGsmaW5zdGFsbFR5cGU9MSZyZXN1bHRUeXBlPTAmZnJvbT1ob21lX3NmMDA0X2NzaWQxNF8wXzMmc3RhcnR5cGU9MQ=='
        req = urllib2.Request(url)
        return req
    
    
    def baiduzhushou_1(self, uid='360F505CC708AB56E4F071B29BC48D65', pingpai='Xiaomi', xinghao='MI%%25', ver='4.1.1'):
        req = {}

        url = 'http://m.baidu.com/app?uid=%s%%257C719800050017453&f=content%%40download%%40506%%402%%406&=&psize=2&usertype=0&ver=16780818&from=1092a&tj=soft_3006428_3115001032_%%E5%%9C%%9F%%E8%%B1%%86&operator=&network=WF&pkname=com.baidu.appsearch&country=CN&gms=false&platform_version_id=16&firstdoc=&action=download&pu=cua%%40480_800_android_4.1.1_240%%2Cosname%%40baiduappsearch%%2Cctv%%401%%2Ccfrom%%401092a%%2Ccuid%%40%s%%25257C719800050017453%%2Ccut%%40%s_%s_%s&language=zh&apn=&'  % (uid, uid, xinghao, ver, pingpai)

        req = urllib2.Request(url)
        return req
    
    def baiduzhushou_2(self):
        req = {}
        
        url = 'http://loc.map.baidu.com/sdk.php'
        
        data = {'qt':'conf', 'req':'4Oqhv6ev6rvm56nmo-T07e6blezrzeDkmOPmkuKWxu7UiKDa-Ibb3Ib3h_OJ3dSJgM3FxcGZwcDLxcTCzMSRxPqb0KCT5r287YNYwqo0TP..|tp=3'}
        
        req['url'] = url
        req['data'] = data
        
        return req
    
    def baiduzhushou_3(self) :

        url = 'http://gdown.baidu.com/data/wisegame/a38745f785e331c0/tudou.apk'
        req = urllib2.Request(url)
        return req
    
    
    def baiduzhushou_4(self):
        req = {}

        url = 'http://loc.map.baidu.com/sdk.php'

        data = {'bloc':'4aGz9_3t-fH7-6Wi7PXv8L3msbCj6-bgsrKh5b2Fqu7V28KJ1rTOgNfchYqA3YvcnMiYncffnZTQmNvajYbJyKH44rfou7nk4r_q6uHg5rX2qfnz46_9_fzy9KOoqqj3lZSSmcHXysWXn8TEyJXAlIuK09-OgsKI1NfR1dTb2IZ1d3ZxLXohYXZ_ISQjIHIlOG0wOGRubGN4NTc3NW1qNwJWXF8KUA0OXRMKUVJSAwBJHkoYRkBFTxEeWxBBHkFCPmxgPWlqaWYxOGguYDVrMn8rfngoK399f3J_fW0qKSERHEFLQxMcTRQUREpLWUMUXwlbDV4ABl5UVVxeAQFF-v6t_fv__f6q8amrrqn1qafp7Lm5u-y877S1srnr4evXmomG3Iza3YTf2oOG1N2Kz5eAmMzPnsnAk56UkMDNw7Swt_m8uL--t7Lp4LDi5-Cg9Kry6en8wPn49-C29sbr2Jucg9qd956Gmp3Bw8mWyoPUjd7fiIqZxIGN29KeiJ4tIig3cHokdzQkI31nLCFxMTxuL2wrZ20WRDY0RWFtHlpULVwreVEJBiNbcAwGVAE5Hz8QGE9CA0AUHx4RQElNPDY9MjluO30_ZTEVAXxPayp-JB9pbH9sfiF7d3M2dmsRZx0TCwheRkYJHVxHV0UcBl8OTx1PBw4RFRQJBQ1Yt722qKO--6HL8qqp5_v7o7e54LCg7LyytKOo5vHwoL2Gn4aFnnU6BT-a|tp=3'}

        req['url'] = url
        req['data'] = data

        return req
    
        
    

def main():
	#anzhuoshichang();
	#anzhuo91();
	pass


if __name__ == '__main__':
	main()

