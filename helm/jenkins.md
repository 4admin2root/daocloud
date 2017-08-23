# install
helm install --name my-jenkins --set Persistence.StorageClass=slow stable/jenkins
# apply jenkins.yml
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: my-jenkins-ingress
spec:
  rules:
  - host: ci-k.xzxpay.com
    http:
      paths:
      - path: /
        backend:
          serviceName: my-release-jenkins
          servicePort: 8080
```

NAME:   my-release
LAST DEPLOYED: Mon Aug 21 11:14:47 2017
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Service
NAME                      CLUSTER-IP     EXTERNAL-IP  PORT(S)         AGE
my-release-jenkins-agent  10.96.122.90   <none>       50000/TCP       1s
my-release-jenkins        10.99.241.104  <pending>    8080:30693/TCP  1s

==> v1beta1/Deployment
NAME                DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
my-release-jenkins  1        1        1           0          0s

==> v1/Secret
NAME                TYPE    DATA  AGE
my-release-jenkins  Opaque  2     1s

==> v1/ConfigMap
NAME                      DATA  AGE
my-release-jenkins        3     1s
my-release-jenkins-tests  1     1s

==> v1/PersistentVolumeClaim
NAME                STATUS   VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
my-release-jenkins  Pending  slow    1s


NOTES:
1. Get your 'admin' user password by running:
  printf $(kubectl get secret --namespace default my-release-jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode);echo
2. Get the Jenkins URL to visit by running these commands in the same shell:
  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        You can watch the status of by running 'kubectl get svc --namespace default -w my-release-jenkins'
  export SERVICE_IP=$(kubectl get svc --namespace default my-release-jenkins --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")
  echo http://$SERVICE_IP:8080/login

3. Login with the password from step 1 and the username: admin

For more information on running Jenkins on Kubernetes, visit:
https://cloud.google.com/solutions/jenkins-on-container-engine

# how to 
1. job Waiting for next available executor
'manage jenkins' - 'manage nodes' - 'master' 
executors: 1  

2. container logs with error:
Aug 22, 2017 8:01:59 AM org.csanchez.jenkins.plugins.kubernetes.KubernetesCloud provision
WARNING: Failed to count the # of live instances on Kubernetes
io.fabric8.kubernetes.client.KubernetesClientException: Failure executing: GET at: https://kubernetes.default/api/v1/namespaces/default/pods?labelSelector=jenkins%3Dslave. Message: Forbidden!Configured service account doesn't have access. Service account may have been revoked.
