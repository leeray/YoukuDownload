#!/usr/bin/env python
# encoding: utf-8
"""
tudouthread.py

Created by 李 瑞 on 2013-05-09.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
import urllib2
import urllib
import random
import time
import threading
import sys
from Queue import Queue
import tudourequesturl


def help():
    print '''
usage: python tudouthread.py 100000 100 anzhuo91

Avaiable arguments:
  argv 1 : request count
  argv 2 : thread count 
  argv 3 : factory type ('anzhuo91' , 'anzhuoshichang' , '360', 'baidu', 'yingyonghui', 'uc', 'jifeng', 'anzhi')
    '''


class TestThread(threading.Thread):
    def run(self):
        global queue
        global whole_url_count
        global which_url
        count = 0
        success_count = 0
        stime = time.time()
        while True:
            if queue.qsize() <= 0:
                break
            else:
                count = count + 1
                req = queue.get()
                try:
                    if isinstance(req, dict):
                        # POST 
                        # print 'POST:', req
                        para_data = ''
                        header = ''
                        if which_url == 'jifeng':
                            para_data = req['data']['Data']
                            header = req['header']
                            request = urllib2.Request(req['url'], para_data, headers=header)
                        else:
                            para_data = urllib.urlencode(req['data'])
                            request = urllib2.Request(req['url'], para_data)
                        
                        response = urllib2.urlopen(request, timeout=20)
                        
                    else:
                        # GET
                        # print 'GET:', req
                        response = urllib2.urlopen(req, timeout=20)
                except urllib2.HTTPError, e:
                    print 'TestThread(', count, ') HTTPError: ', e
                except urllib2.URLError, e:
                    print 'TestThread(', count, ') URLError: ', e
                else:
                    #the_page = response.read()
                    success_count = success_count + 1
            
            
            print 'q.size():', queue.qsize(), '   whole_url_count:', whole_url_count
            if (queue.qsize() % whole_url_count) != 0:
                # print '不沉睡。同一请求.'
                continue
            else:
                sleeptime = random.randint(1,10)
                # print '沉睡%s秒.' % sleeptime
                time.sleep(sleeptime)
            
        etime = time.time()
        print 'TestThread(',count, ') success_count : ', success_count, '  operation time:%ss' % str(etime-stime)

request_count = 10000
thread_count = 10
which_url = '360'
whole_url_count = 1
queue = Queue()

def test():
    global whole_url_count, which_url
    
    dy = tudourequesturl.DownloadTudou();
    
    for i in range(int(request_count)):
        index_model = random.randint(0, len(dy._model)-1)
        index_nettype = random.randint(0, len(dy._nettype)-1)
        index_ver = random.randint(0, len(dy._ver)-1)

        nettype = dy._nettype[index_nettype]
        model = dy._model[index_model]
        imei = str(random.randint(0,999999999999999))
        imsi = str(random.randint(0,999999999999999))
        mac = ':'.join([''.join(str('%02x' % random.randint(0,255))) for i in range(6)])
        uid = ''.join([random.choice('QWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(32)])
        ver = dy._ver[index_ver]
        ip = '.'.join([str(random.randint(0,254)) for i in range(4)])
        
        #print 'model:', model, '  nettype:', nettype, '  imei:', imei, '  imsi:', imsi, '  mac:', mac
        b = True
        if which_url == 'anzhuo91' :
            req = dy.anzhuo91_1(dm=model, imei=imei, imsi=imsi, mac=mac)
            queue.put(req)
            
            req = dy.anzhuo91_2(dm=model, imei=imei, imsi=imsi, mac=mac)
            queue.put(req)
            
            # req = dy.anzhuo91_3(dm=model, imei=imei, imsi=imsi, mac=mac)
            # queue.put(req)
            
            req = dy.anzhuo91_4(dm=model, imei=imei, imsi=imsi, mac=mac)
            queue.put(req)
            
            whole_url_count = 3
            
        elif which_url == 'anzhuoshichang':
            req = dy.anzhuoshichang(nettype=nettype, model=model)
            queue.put(req)
            
            whole_url_count = 1 
            
        elif which_url == '360':
            req = dy.shouji360_1()
            queue.put(req)
            
            req = dy.shouji360_2()
            queue.put(req)
            
            whole_url_count = 2
            
        elif which_url == 'baidu':
            req = dy.baiduzhushou_1(uid=uid, pingpai=model.split(' ')[0], xinghao=''.join(model.split(' ')[1:]), ver=ver)
            queue.put(req)

            req = dy.baiduzhushou_2()
            queue.put(req)

            # req = dy.baiduzhushou_3()
            # queue.put(req)
            
            req = dy.baiduzhushou_4()
            queue.put(req)
            
            whole_url_count = 3
        
        elif which_url == 'yingyonghui':
            req = dy.yingyonghui_1()
            queue.put(req)
            
            req = dy.yingyonghui_2()
            queue.put(req)
            
            req = dy.yingyonghui_3()
            queue.put(req)
            
            req = dy.yingyonghui_4()
            queue.put(req)
            
            req = dy.yingyonghui_5()
            queue.put(req)
            
            req = dy.yingyonghui_6()
            queue.put(req)
            
            req = dy.yingyonghui_7()
            queue.put(req)
            
            whole_url_count = 7
        
        elif which_url == 'uc':
            req = dy.uc_1()
            queue.put(req)
            
            req = dy.uc_2()
            queue.put(req)
            
            whole_url_count = 2
        
        elif which_url == 'jifeng':
            req = dy.jifeng_1(model=model.replace(' ', '-'), mac=mac)
            queue.put(req)
            
            req = dy.jifeng_2(model=model.replace(' ', '-'), mac=mac)
            queue.put(req)
            
            req = dy.jifeng_3(model=model.replace(' ', '-'), mac=mac)
            queue.put(req)
            
            req = dy.jifeng_4(model=model.replace(' ', '-'), mac=mac)
            queue.put(req)
            
            req = dy.jifeng_5(model=model.replace(' ', '-'), mac=mac, ip=ip)
            queue.put(req)
            
            req = dy.jifeng_6(model=model.replace(' ', '-'), mac=mac, ip=ip)
            queue.put(req)
            
            whole_url_count = 6
            
        elif which_url == 'anzhi':
            req = dy.anzhi_1()
            queue.put(req)
            
            whole_url_count = 1
        
        else:
            help();
            sys.exit();
        
    for i in range(int(thread_count)):
        p = TestThread()
        p.start()


if __name__ == '__main__':
    if(len(sys.argv)) < 4:
        help()
        sys.exit()
    request_count = sys.argv[1]
    thread_count = sys.argv[2]
    which_url = sys.argv[3]
    
    print 'request_count:', request_count, ',  threadcount:', thread_count, ',  factorytype:', which_url
    test()
