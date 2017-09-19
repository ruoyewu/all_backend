import pymysql

host = 'localhost'
username = 'root'
password = 'ILYT3421'
db_name = 'allapp'

insert_sql = "insert into article values('%s', '%s')"

query_sql = "select * from article WHERE `key`= '%s'"


def put_article(key, content):
    conn, cur = openDB()
    # print(key, content.encode().decode())
    try:
        cur.execute(insert_sql % (key, content))
        conn.commit()
    except:
        print('error')
    finally:
        closeDB(conn, cur)
    pass


def get_article(key):
    conn, cur = openDB()
    try:
        cur.execute(query_sql % key)
        result = cur.fetchone()[1]
    except:
        result = 'no'

    closeDB(conn, cur)
    return result


def openDB():
    conn = pymysql.connect(host=host, user=username, passwd=password, db=db_name, charset='utf8mb4')
    cur = conn.cursor()
    return conn, cur


def closeDB(conn, cur):
    cur.close()
    conn.close()


if __name__ == "__main__":
    put_article('哈哈', '哈哈')

