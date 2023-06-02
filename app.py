import dbcreds
import mariadb

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()
