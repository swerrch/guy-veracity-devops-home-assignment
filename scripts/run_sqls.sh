#/bin/bash!


ENTRY_PATH='/docker-entrypoint-initdb.d'
POOL_CONF_PATH='/opt/bitnami/pgpool/conf'

echo "local     all             all                         scram-sha-256" >> $POOL_CONF_PATH/pool_hba.conf

PGPASSWORD=adminpassword psql -d postgres -U postgres -h localhost -f $ENTRY_PATH/create_rw_user.sql
PGPASSWORD=adminpassword psql -d postgres -U postgres -h localhost -f $ENTRY_PATH/create_ro_user.sql

pg_enc -m -f $POOL_CONF_PATH/pgpool.conf -k $POOL_CONF_PATH/.pgpoolkey -i $ENTRY_PATH/users.txt

pgpool -f $POOL_CONF_PATH/pgpool.conf  -k $POOL_CONF_PATH/.pgpoolkey -a $POOL_CONF_PATH/pool_hba.conf reload
