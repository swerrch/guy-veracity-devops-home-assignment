from configparser import ConfigParser

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

CONFIG_CONNECTION = './database.ini'
CONFIG_POSTGRES_SECTION = 'postgresql'
CONFIG_RW_USER_SECTION = 'rw_user'


def config(section, filename=CONFIG_CONNECTION):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def execute_sql(configuration, sql_file):
    conn = None
    try:
        params = config(configuration)

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        with cur as cursor:
            cursor.execute(open(sql_file, "r").read())

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        raise Exception(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    execute_sql(CONFIG_POSTGRES_SECTION, './sql/create_rw_user.sql')
    execute_sql(CONFIG_RW_USER_SECTION, './sql/create_ro_user.sql')
