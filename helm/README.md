# install helm  
http://www.jianshu.com/p/1953b86649df
## download helm
```
wget https://storage.googleapis.com/kubernetes-helm/helm-v2.6.0-linux-amd64.tar.gz
tar -xvf helm-v2.6.0-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/
rm -rf linux-amd64
```
## run helm
```
helm init --service-account tiller --tiller-image 4admin2root/tiller:v2.6.0 --upgrade
```
## create sa
```
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
```
# check tiller in k8s
tiller-deploy-3864618634-gjqn7                             1/1       Running   0          8m        10.32.0.60   

➜  ~ helm version
Client: &version.Version{SemVer:"v2.6.0", GitCommit:"5bc7c619f85d74702e810a8325e0a24f729aa11a", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.6.0", GitCommit:"5bc7c619f85d74702e810a8325e0a24f729aa11a", GitTreeState:"clean"}

# for example:
```
helm search jenkins
helm install --name my-release --set Persistence.StorageClass=slow stable/jenkins
helm get my-release
```
