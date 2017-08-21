# install
```
wget https://raw.githubusercontent.com/kubernetes/charts/master/stable/gitlab-ce/values.yaml
# change the value in values.yml if necessary
helm install --name my-gitlab -f gitlab_values.yaml stable/gitlab-ce
```
NAME:   my-gitlab
LAST DEPLOYED: Mon Aug 21 14:48:39 2017
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/PersistentVolumeClaim
NAME                      STATUS   VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
my-gitlab-postgresql      Pending  slow    2s
my-gitlab-redis           Pending  slow    2s
my-gitlab-gitlab-ce-data  Pending  slow    2s
my-gitlab-gitlab-ce-etc   Pending  slow    2s

==> v1/Service
NAME                  CLUSTER-IP     EXTERNAL-IP  PORT(S)                                  AGE
my-gitlab-postgresql  10.103.81.44   <none>       5432/TCP                                 1s
my-gitlab-redis       10.103.165.68  <none>       6379/TCP                                 1s
my-gitlab-gitlab-ce   10.101.49.79   <pending>    22:31573/TCP,80:31484/TCP,443:31039/TCP  1s

==> v1beta1/Deployment
NAME                  DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
my-gitlab-postgresql  1        1        1           0          1s
my-gitlab-redis       1        1        1           0          1s
my-gitlab-gitlab-ce   1        1        1           0          1s

==> v1/Secret
NAME                  TYPE    DATA  AGE
my-gitlab-postgresql  Opaque  1     2s
my-gitlab-redis       Opaque  1     2s
my-gitlab-gitlab-ce   Opaque  4     2s

==> v1/ConfigMap
NAME                 DATA  AGE
my-gitlab-gitlab-ce  1     2s


NOTES:

1. Get your GitLab URL by running:

  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        Watch the status with: 'kubectl get svc -w my-gitlab-gitlab-ce'

  export SERVICE_IP=$(kubectl get svc --namespace default my-gitlab-gitlab-ce -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
  echo http://$SERVICE_IP/

2. Login as the root user:

  Username: root
  Password: Passw0rd


3. Point a DNS entry at your install to ensure that your specified
   external URL is reachable:

   http://git-k.xzxpay.com/
