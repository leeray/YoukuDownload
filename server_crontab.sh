#!/bin/sh

cd /opt/leeray/YoukuDownload

cmd_360="nohup python testthread.py 400000 100 360 > ./Logs/360_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_360

cmd_anzhuo91="nohup python testthread.py 400000 100 anzhuo91 > ./Logs/anzhuo91_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_anzhuo91

cmd_anzhuoshichang="nohup python testthread.py 400000 100 anzhuoshichang > ./Logs/anzhuoshichang_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_anzhuoshichang

cmd_baidu="nohup python testthread.py 400000 100 baidu > ./Logs/baidu_`date +\%Y\%m\%d`.log 2>&1 &"
echo $cmd_baidu

`$cmd_360`
`$cmd_anzhuo91`
`$cmd_anzhuoshichang`
`$cmd_baidu`


