import pymysql


host = 'localhost'
username = 'root'
password = 'ruoyetian'
db_name = 'allapp'


def openDB():
    conn = pymysql.connect(host=host, user=username, passwd=password, db=db_name, charset='utf8mb4')
    cur = conn.cursor()
    return conn, cur


def closeDB(conn, cur):
    cur.close()
    conn.close()