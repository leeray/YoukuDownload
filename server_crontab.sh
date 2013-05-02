#!/bin/sh

cd /opt/leeray/YoukuDownload

cmd_360="python testthread.py 400000 100 360 > Logs/360_`date +\%Y\%m\%d`.log"
echo $cmd_360

cmd_anzhuo91="python testthread.py 400000 100 anzhuo91 > Logs/anzhuo91_`date +\%Y\%m\%d`.log"
echo $cmd_anzhuo91

cmd_anzhuoshichang="python testthread.py 400000 100 anzhuoshichang > Logs/anzhuoshichang_`date +\%Y\%m\%d`.log"
echo $cmd_anzhuoshichang

cmd_baidu="python testthread.py 400000 100 baidu > Logs/baidu_`date +\%Y\%m\%d`.log"
echo $cmd_baidu

`nohup $cmd_360`
`nohup $cmd_anzhuo91`
`nohup $cmd_anzhuoshichang`
`nohup $cmd_baidu`


