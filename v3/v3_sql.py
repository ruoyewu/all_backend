import pymysql

host = 'localhost'
username = 'root'
password = 'ILYT3421'
db_name = 'allapp'

insert_article_sql = "insert into article values('%s', '%s')"
insert_user_sql = "insert into user (name, password, email, phone) values('%s', '%s', '%s', '%s')"
insert_comment_sql = "insert into comment (time, username, content, `key`, parent) values " \
                     "('%d', '%s', '%s', '%s', '%d')"

query_article_sql = "select * from article WHERE `key`= '%s'"
query_user_name_sql = "select * from user WHERE name = '%s'"
query_user_id_sql = "select * from user WHERE id = '%d'"
query_comment_sql = "select * from comment WHERE `key` = '%s' ORDER BY `time` desc limit 10"
query_comment_below_sql = "select * from comment WHERE `key` = '%s' and `time` < '%d' order by `time` desc limit 10"
query_comment_id_sql = "select * from comment WHERE  id = '%d'"
query_comment_time_user_sql = "select * from comment WHERE time = '%d' and username = '%s'"


def put_article(key, content):
    conn, cur = openDB()
    try:
        cur.execute(insert_article_sql % (key, content))
        conn.commit()
    except:
        print('error')
    finally:
        closeDB(conn, cur)
    pass


def get_article(key):
    conn, cur = openDB()
    try:
        cur.execute(query_article_sql % key)
        result = cur.fetchone()[1]
    except:
        result = 'no'

    closeDB(conn, cur)
    return result


def put_user(name, pwd, email, phone):

    conn, cur = openDB()
    try:
        cur.execute(insert_user_sql % (name, pwd, email, phone))
        conn.commit()
        result = 'ok'
    except:
        result = 'error'

    closeDB(conn, cur)
    return result


def get_user(data):
    id = data['id']
    name = data['name']
    conn, cur = openDB()

    if id == -1:
        cur.execute(query_user_name_sql % name)
    else:
        cur.execute(query_user_id_sql % id)
    result = cur.fetchone()
    if result is None:
        result = 'no'

    closeDB(conn, cur)
    return result


def put_comment(time, username, content, key, parent):
    conn, cur = openDB()

    try:
        cur.execute(insert_comment_sql % (time, username, content, key, parent))
        conn.commit()
        result = 'ok'
    except:
        result = 'error'

    closeDB(conn, cur)
    return result


def get_comment(key, below):
    conn, cur = openDB()

    if below != 0:
        cur.execute(query_comment_below_sql % (key, below))
    else:
        cur.execute(query_comment_sql % (key))
    result = cur.fetchall()

    closeDB(conn, cur)
    return result


def get_comment_id(id):
    conn, cur = openDB()

    cur.execute(query_comment_id_sql % (id))
    result = cur.fetchone()

    if result is None:
        result = 'no'

    closeDB(conn, cur)
    return result


def get_comment_time_username(time, username):
    conn, cur = openDB()
    cur.execute(query_comment_time_user_sql % (time, username))
    result = cur.fetchone()

    if result is None:
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
    print(get_comment_id(17))
