# DevOps Home Assignment
The project consists of a `docker-compose` configuration for High Availability PostgreSQL cluster.

## Architecture
The cluster holds 3 `postgresql-repmgr` instances, whence one instance is primary and 2 are standbies. There is a `load-balancer` `pgpool` instance which ensures the connecions to the nodes. And an instance of `pgAdmin4` web client that is runnins on:
```
localhost:5050
```

## Deploy
#### Requirments:
  - Docker
#### For deploying the cluster clone the repo and execute:
```bash
docker-compose up
```
or 
```bash
docker-compose up -d
```
