#!/bin/sh

cd /opt/leeray/YoukuDownload

cmd_360="nohup python tudouthread.py 100000 100 360 > ./Logs/tudou_360_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_360
nohup python tudouthread.py 200000 100 360 > ./Logs/tudou_360_`date +\%Y\%m\%d`.log 2>&1 &

cmd_anzhuo91="nohup python tudouthread.py 100000 100 anzhuo91 > ./Logs/tudou_anzhuo91_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_anzhuo91
nohup python tudouthread.py 200000 100 anzhuo91 > ./Logs/tudou_anzhuo91_`date +\%Y\%m\%d`.log 2>&1 &

cmd_anzhuoshichang="nohup python tudouthread.py 100000 100 anzhuoshichang > ./Logs/tudou_anzhuoshichang_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_anzhuoshichang
nohup python tudouthread.py 200000 100 anzhuoshichang > ./Logs/tudou_anzhuoshichang_`date +\%Y\%m\%d`.log 2>&1 &

cmd_baidu="nohup python tudouthread.py 100000 100 baidu > ./Logs/tudou_baidu_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_baidu
nohup python tudouthread.py 200000 100 baidu > ./Logs/tudou_baidu_`date +\%Y\%m\%d`.log 2>&1 &

cmd_jifeng="nohup python tudouthread.py 100000 100 jifeng > ./Logs/tudou_jifeng_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_jifeng
nohup python tudouthread.py 200000 100 jifeng > ./Logs/tudou_jifeng_`date +\%Y\%m\%d`.log 2>&1 &

cmd_uc="nohup python tudouthread.py 100000 100 uc > ./Logs/tudou_uc_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_uc
nohup python tudouthread.py 200000 100 uc > ./Logs/tudou_uc_`date +\%Y\%m\%d`.log 2>&1 &

cmd_anzhi="nohup python tudouthread.py 100000 100 anzhi > ./Logs/tudou_anzhi_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_anzhi
nohup python tudouthread.py 200000 100 anzhi > ./Logs/tudou_anzhi_`date +\%Y\%m\%d`.log 2>&1 &

cmd_yingyonghui="nohup python tudouthread.py 100000 100 yingyonghui > ./Logs/tudou_yingyonghui_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_yingyonghui
nohup python tudouthread.py 200000 100 yingyonghui > ./Logs/tudou_yingyonghui_`date +\%Y\%m\%d`.log 2>&1 &


