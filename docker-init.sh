#!/bin/bash
sed -i 's/10.8.32.30:8080/mirrors\.aliyun\.com/' /etc/yum.repos.d/CentOS-Base.repo
sed -i 's/10.8.32.30:8080/mirrors\.aliyun\.com/' /etc/yum.repos.d/epel.repo
yum install docker-1.12.6 -y
systemctl enable docker
sed -i 's/ExecStart=\/usr\/bin\/dockerd-current/ExecStart=\/usr\/bin\/dockerd-current --registry-mirror=https:\/\/m1empwb1.mirror.aliyuncs.com/' /usr/lib/systemd/system/docker.service
systemctl daemon-reload
systemctl restart docker
