# install
helm install --name my-redis \
  --set redisPassword=secretpassword,persistence.storageClass=slow \
    stable/redis

# result
NAME:   my-redis
LAST DEPLOYED: Wed Aug 23 10:04:59 2017
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Secret
NAME            TYPE    DATA  AGE
my-redis-redis  Opaque  1     0s

==> v1/PersistentVolumeClaim
NAME            STATUS   VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
my-redis-redis  Pending  slow    0s

==> v1/Service
NAME            CLUSTER-IP    EXTERNAL-IP  PORT(S)   AGE
my-redis-redis  10.99.224.92  <none>       6379/TCP  0s

==> v1beta1/Deployment
NAME            DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
my-redis-redis  1        0        0           0          0s


NOTES:
Redis can be accessed via port 6379 on the following DNS name from within your cluster:
my-redis-redis.default.svc.cluster.local
To get your password run:

    REDIS_PASSWORD=$(kubectl get secret --namespace default my-redis-redis -o jsonpath="{.data.redis-password}" | base64 --decode)

To connect to your Redis server:

1. Run a Redis pod that you can use as a client:

   kubectl run my-redis-redis-client --rm --tty -i --env REDIS_PASSWORD=$REDIS_PASSWORD --image bitnami/redis:3.2.9-r2 -- bash

2. Connect using the Redis CLI:

  redis-cli -h my-redis-redis -a $REDIS_PASSWORD

