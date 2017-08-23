# install
helm install --name myblog \
  --set wordpressUsername=admin,wordpressPassword=Passw0rd,mariadb.mariadbRootPassword=secretpassword,persistence.storageClass=slow,persistence.size=1Gi,mariadb.persistence.storageClass=slow,mariadb.persistence.size=3Gi,ingress.enabled=true,ingress.hostname=opsblog-k.xzxpay.com \
    stable/wordpress
# result

NAME:   myblog
LAST DEPLOYED: Wed Aug 23 10:59:09 2017
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Secret
NAME              TYPE    DATA  AGE
myblog-mariadb    Opaque  2     2s
myblog-wordpress  Opaque  2     1s

==> v1/ConfigMap
NAME            DATA  AGE
myblog-mariadb  1     1s

==> v1/PersistentVolumeClaim
NAME              STATUS   VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
myblog-mariadb    Pending  slow    1s
myblog-wordpress  Pending  slow    1s

==> v1/Service
NAME              CLUSTER-IP     EXTERNAL-IP  PORT(S)                     AGE
myblog-mariadb    10.105.158.68  <none>       3306/TCP                    1s
myblog-wordpress  10.97.231.195  <pending>    80:30712/TCP,443:31418/TCP  1s

==> v1beta1/Deployment
NAME              DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
myblog-mariadb    1        1        1           0          1s
myblog-wordpress  1        1        1           0          1s

==> v1beta1/Ingress
NAME              HOSTS                 ADDRESS  PORTS  AGE
myblog-wordpress  opsblog-k.xzxpay.com  80       1s


NOTES:
1. Get the WordPress URL:

  You should be able to access your new WordPress installation through

  http://opsblog-k.xzxpay.com/admin

2. Login with the following credentials to see your blog

  echo Username: admin
  echo Password: $(kubectl get secret --namespace default myblog-wordpress -o jsonpath="{.data.wordpress-password}" | base64 --decode)
