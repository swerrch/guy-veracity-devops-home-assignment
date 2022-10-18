CREATE USER rw_user WITH PASSWORD 'rw_user';

GRANT CONNECT ON DATABASE customdatabase TO rw_user;

GRANT USAGE, CREATE ON SCHEMA public TO rw_user;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO rw_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO rw_user;