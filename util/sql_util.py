import pymysql


host = 'localhost'
username = 'debian-sys-maint'
password = 'NfGi6vUSCsMIZyqt'
db_name = 'all'


def openDB():
    conn = pymysql.connect(host=host, user=username, passwd=password, db=db_name, charset='utf8mb4')
    cur = conn.cursor()
    return conn, cur


def closeDB(conn, cur):
    cur.close()
    conn.close()