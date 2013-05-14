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

    def yingyonghui_1(self) :
        req = {}

        url = 'http://mobile.appchina.com/market/api'
        data = {'key':'',
        'referer':'ce9f14f2-827c-4cbc-9474-d91bd1438d45',
        'api':'market.MarketAPI',
        'deviceId':'354710050008917',
        'param':'{"id":895425,"guid":"ce9f14f2-827c-4cbc-9474-d91bd1438d45","type":"app.detail","apiVer":"2","gpuType":4}'}

        req['url'] = url
        req['data'] = data
        return req

    def yingyonghui_2(self) :
        req = {}
        url = 'http://mobile.appchina.com/market/api'
        data = {'key':'',
        'referer':'ce9f14f2-827c-4cbc-9474-d91bd1438d45',
        'api':'market.MarketAPI',
        'deviceId':'354710050008917',
        'param':'{"guid":"ce9f14f2-827c-4cbc-9474-d91bd1438d45","appid":895425,"type":"accountcomment.list","start":0,"apiVer":"2","size":10}'}

        req['url'] = url
        req['data'] = data
        return req

    def yingyonghui_3(self) :

        url = 'http://mobile.appchina.com/market/e/895425/0/0/0/package_18.apk?channel=ac.ex.BaiduWL&ug=0&ct=1368412429697&p=Detail&r=Category&i=25&k=download.306'
        req = urllib2.Request(url)
        return req

    def yingyonghui_4(self) :

        url = 'http://mobile.d.appchina.com/McDonald/e/895425/0/0/0/package_18.apk?channel=ac.ex.BaiduWL&ug=0&ct=1368412429697&p=Detail&r=Category&i=25&k=download.306'
        req = urllib2.Request(url)
        return req

    def yingyonghui_5(self) :

        url = 'http://fast.yingyonghui.com/19f9bcca62a65fd3df20878fdd288c3c/5190433c/apk/895425/com.tudou.android.1367803319807.apk'
        req = urllib2.Request(url)
        return req

    def yingyonghui_6(self) :
        req = {}
        url = 'http://mobile.appchina.com/market/api'
        data = {'key':'',
        'referer':'ce9f14f2-827c-4cbc-9474-d91bd1438d45',
        'api':'market.MarketAPI',
        'deviceId':'354710050008917',
        'param':'{"guid":"ce9f14f2-827c-4cbc-9474-d91bd1438d45","appid":895425,"type":"accountcomment.list","start":0,"apiVer":"2","size":10}'}

        req['url'] = url
        req['data'] = data
        return req

    def yingyonghui_7(self) :
        req = {}
        url = 'http://openbox.mobilem.360.cn/mintf/getAppsByPackNames'
        data = {'ks':'com.tudou.android|18|0|土豆&type=2&os=16&i=d6ed1263129ac06c6b21102763de7931',
        'type':'2',
        'os':'16',
        'i':'d6ed1263129ac06c6b21102763de7931'}

        req['url'] = url
        req['data'] = data
        return req

    def uc_1(self):
        url = 'http://s1.app.uc.cn/pack/2013/05/10/Tudou_Android_3.1_ucweb.apk'
        req = urllib2.Request(url)
        return req


    def uc_2(self) :
        req = {}
        url = 'http://m.app.uc.cn/apk/api/1.1/stat/download.json?source=client'
        data = {'':''}

        req['url'] = url
        req['data'] = data
        return req

    def jifeng_1(self, nettype='WIFI', model='MI-2', mac='c4:6a:b7:4e:e3:36', device='867064014692428'):
        req = {}
        headers = {'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.2; %s Build/JZO54K)' % model
        ,'Connection': 'Keep-Alive'
        ,'Host': 'api.gfan.com'
        ,'G-Header': '%s/4.1.2/aMarket2.0/0.9.7beta/9/354710050008917/null/%s' % (model, mac)
        }
        url = 'http://api.gfan.com/market/api/getProductDetail'
        data = {'Data':'<request version="2" local_version="-1"><p_id>16902</p_id><source_type>0</source_type></request>'}
        req['url'] = url
        req['data'] = data
        req['header'] = headers
        return req

    def jifeng_2(self, nettype='WIFI', model='MI-2', mac='c4:6a:b7:4e:e3:36', device='867064014692428'):
        req = {}
        headers = {'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.2; %s Build/JZO54K)' % model
        ,'Connection': 'Keep-Alive'
        ,'Host': 'api.gfan.com'
        ,'G-Header': '%s/4.1.2/aMarket2.0/0.9.7beta/9/354710050008917/null/%s' % (model, mac)
        }
        url = 'http://api.gfan.com/market/api/tagsByApp'
        data = {'Data':'<request version="2"><p_id>16902</p_id><screen_size>480#800</screen_size><match_type>1</match_type><platform>16</platform></request>'}
        req['url'] = url
        req['data'] = data
        req['header'] = headers
        return req

    def jifeng_3(self, nettype='WIFI', model='MI-2', mac='c4:6a:b7:4e:e3:36', device='867064014692428'):
        req = {}
        headers = {'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.2; %s Build/JZO54K)' % model
        ,'Connection': 'Keep-Alive'
        ,'Host': 'api.gfan.com'
        ,'G-Header': '%s/4.1.2/aMarket2.0/0.9.7beta/9/354710050008917/null/%s' % (model, mac)
        }
        url = 'http://api.gfan.com/market/api/getDownloadUrl'
        data = {'Data':'<request version="2"><p_id>16902</p_id><uid></uid><source_type>0</source_type></request>'}
        req['url'] = url
        req['data'] = data
        req['header'] = headers
        return req

    def jifeng_4(self, nettype='WIFI', model='MI-2', mac='c4:6a:b7:4e:e3:36', device='867064014692428'):
        url = 'http://cdn2.down.apk.gfan.com/asdf/Pfiles/2013/5/6/16902_f2d99353-1174-42f1-99ea-5764c76d3561.apk'
        req = urllib2.Request(url)
        return req

    def jifeng_5(self, nettype='WIFI', model='MI-2', mac='c4:6a:b7:4e:e3:36', device='867064014692428', ip='61.147.122.97'):
        req = {}
        headers = {'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.2; %s Build/JZO54K)' % model
        ,'Connection': 'Keep-Alive'
        ,'Host': 'api.gfan.com'
        ,'G-Header': '%s/4.1.2/aMarket2.0/0.9.7beta/9/354710050008917/null/%s' % (model, mac)
        }
        url = 'http://api.gfan.com/market/api/downReport'
        data = {'Data':'<request version="2"><uid>-1</uid><package_name>com.tudou.android</package_name><report_type>0</report_type><source_type>0</source_type><cpid>web261</cpid><p_id></p_id><url>http://cdn2.down.apk.gfan.com/asdf/Pfiles/2013/5/6/16902_f2d99353-1174-42f1-99ea-5764c76d3561.apk</url><size>0</size><net_context>network is wifi</net_context><ip>%s</ip></request>' % ip}
        req['url'] = url
        req['data'] = data
        req['header'] = headers
        return req

    def jifeng_6(self, nettype='WIFI', model='MI-2', mac='c4:6a:b7:4e:e3:36', device='867064014692428', ip='61.147.122.97'):
        req = {}
        headers = {'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.2; %s Build/JZO54K)' % model
        ,'Connection': 'Keep-Alive'
        ,'Host': 'api.gfan.com'
        ,'G-Header': '%s/4.1.2/aMarket2.0/0.9.7beta/9/354710050008917/null/%s' % (model, mac)
        }
        url = 'http://api.gfan.com/market/api/downReport'
        data = {'Data':'<request version="2"><uid>-1</uid><package_name></package_name><report_type>1</report_type><source_type>0</source_type><cpid>web261</cpid><p_id></p_id><url>http://cdn2.down.apk.gfan.com/asdf/Pfiles/2013/5/6/16902_f2d99353-1174-42f1-99ea-5764c76d3561.apk</url><size>7743407</size><net_context>network is wifi</net_context><ip>%s</ip></request>' % ip}
        req['url'] = url
        req['data'] = data
        req['header'] = headers
        return req


    def anzhi_1(self):
        url = 'http://am.apk.anzhi.com/apk/201305/02/com.tudou.android_05130700_0.apk?vcode=4310&nettype=WIFI&wap=WIFI'
        req = urllib2.Request(url)
        return req


def main():
	#anzhuoshichang();
	#anzhuo91();
	pass


if __name__ == '__main__':
	main()

