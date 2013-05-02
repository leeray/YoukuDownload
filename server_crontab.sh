#!/bin/sh

cd /opt/leeray/YoukuDownload

cmd_360="python testthread.py 400000 100 360"
echo $cmd_360

cmd_anzhuo91="python testthread.py 400000 100 anzhuo91"
echo $cmd_anzhuo91

cmd_anzhuoshichang="python testthread.py 400000 100 anzhuoshichang"
echo $cmd_anzhuoshichang

cmd_baidu="python testthread.py 400000 100 baidu"
echo $cmd_baidu

`nohup $cmd_360`
`nohup $cmd_anzhuo91`
`nohup $cmd_anzhuoshichang`
`nohup $cmd_baidu`


