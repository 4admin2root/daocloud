docker pull 4admin2root/kube-controller-manager-amd64:v1.6.0
docker pull 4admin2root/kube-scheduler-amd64:v1.6.0
docker pull 4admin2root/kube-apiserver-amd64:v1.6.0
docker pull 4admin2root/etcd-amd64:3.0.17
docker pull 4admin2root/kube-proxy-amd64:v1.6.0
docker pull  4admin2root/k8s-dns-sidecar-amd64:1.14.1
docker pull  4admin2root/k8s-dns-dnsmasq-nanny-amd64:1.14.1
docker pull  4admin2root/pause-amd64:3.0
docker pull 4admin2root/etcd:2.2.1
docker pull 4admin2root/node:v1.1.0
docker pull 4admin2root/cni:v1.6.1
docker pull 4admin2root/kube-policy-controller:v0.5.4
docker tag 4admin2root/kube-controller-manager-amd64:v1.6.0    gcr.io/google_containers/kube-controller-manager-amd64:v1.6.0
docker tag 4admin2root/kube-scheduler-amd64:v1.6.0             gcr.io/google_containers/kube-scheduler-amd64:v1.6.0
docker tag 4admin2root/kube-apiserver-amd64:v1.6.0             gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
docker tag 4admin2root/etcd-amd64:3.0.17                       gcr.io/google_containers/etcd-amd64:3.0.17
docker tag 4admin2root/kube-proxy-amd64:v1.6.0                 gcr.io/google_containers/kube-proxy-amd64:v1.6.0
docker tag  4admin2root/k8s-dns-sidecar-amd64:1.14.1           gcr.io/google_containers/k8s-dns-sidecar-amd64:1.14.1 
docker tag  4admin2root/k8s-dns-dnsmasq-nanny-amd64:1.14.1     gcr.io/google_containers/k8s-dns-dnsmasq-nanny-amd64:1.14.1
docker tag  4admin2root/pause-amd64:3.0                        gcr.io/google_containers/pause-amd64:3.0
docker tag  4admin2root/etcd:2.2.1                             gcr.io/google_containers/etcd:2.2.1
docker tag  4admin2root/node:v1.1.0   quay.io/calico/node:v1.1.0
docker tag  4admin2root/cni:v1.6.1    quay.io/calico/cni:v1.6.1
docker tag  4admin2root/kube-policy-controller:v0.5.4  quay.io/calico/kube-policy-controller:v0.5.4
