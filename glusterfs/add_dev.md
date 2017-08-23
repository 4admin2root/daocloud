# node list
```
[root@cloud4ourself-k8sprod6 ~]# heketi-cli  --server http://10.9.5.64:8080 --user admin --secret heketi_secret node list
Id:7cf6f240dd22b1ed1d5651c1807249cc	Cluster:1249abb80755eb4d376baf1630015abf
Id:9b9b70b4744e154018f113d73eb3d239	Cluster:1249abb80755eb4d376baf1630015abf
Id:ba964d3e19e1b38e4bccec41e27047ea	Cluster:1249abb80755eb4d376baf1630015abf
Id:edca22a57e8999049f09a2b7d23602d9	Cluster:1249abb80755eb4d376baf1630015abf
```
# add dev
```
heketi-cli  --server http://10.9.5.64:8080 --user admin --secret heketi_secret device add \
      --name=/dev/vdd \
      --node=7cf6f240dd22b1ed1d5651c1807249cc
heketi-cli  --server http://10.9.5.64:8080 --user admin --secret heketi_secret device add \
      --name=/dev/vdd \
      --node=9b9b70b4744e154018f113d73eb3d239
heketi-cli  --server http://10.9.5.64:8080 --user admin --secret heketi_secret device add \
      --name=/dev/vdd \
      --node=ba964d3e19e1b38e4bccec41e27047ea
heketi-cli  --server http://10.9.5.64:8080 --user admin --secret heketi_secret device add \
      --name=/dev/vdd \
      --node=edca22a57e8999049f09a2b7d23602d9
```
