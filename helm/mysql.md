# install
helm install --name my-sql --set mysqlLRootPassword=secretpassword,mysqlUser=my-user,mysqlPassword=my-password,mysqlDatabase=my-database,persistence.storageClass=slow  stable/mysql

# result
NAME:   my-sql
LAST DEPLOYED: Mon Aug 21 23:25:36 2017
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/PersistentVolumeClaim
NAME          STATUS   VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
my-sql-mysql  Pending  slow    0s

==> v1/Service
NAME          CLUSTER-IP      EXTERNAL-IP  PORT(S)   AGE
my-sql-mysql  10.102.105.205  <none>       3306/TCP  0s

==> v1beta1/Deployment
NAME          DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
my-sql-mysql  1        0        0           0          0s

==> v1/Secret
NAME          TYPE    DATA  AGE
my-sql-mysql  Opaque  2     0s


NOTES:
MySQL can be accessed via port 3306 on the following DNS name from within your cluster:
my-sql-mysql.default.svc.cluster.local

To get your root password run:

    kubectl get secret --namespace default my-sql-mysql -o jsonpath="{.data.mysql-root-password}" | base64 --decode; echo

To connect to your database:

1. Run an Ubuntu pod that you can use as a client:

    kubectl run -i --tty ubuntu --image=ubuntu:16.04 --restart=Never -- bash -il

2. Install the mysql client:

    $ apt-get update && apt-get install mysql-client -y

3. Connect using the mysql cli, then provide your password:
    $ mysql -h my-sql-mysql -p
