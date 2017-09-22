import pymysql

host = 'localhost'
username = 'root'
password = 'ILYT3421'
db_name = 'allapp'

insert_article_sql = "insert into article values('%s', '%s')"
query_article_sql = "select * from article WHERE `key`= '%s'"

insert_user_sql = "insert into user (name, password, email, phone) values('%s', '%s', '%s', '%s')"
query_user_name_sql = "select * from user WHERE name = '%s'"
query_user_id_sql = "select * from user WHERE id = '%d'"

insert_comment_sql = "insert into comment (time, username, content, `key`, parent) values " \
                     "('%d', '%s', '%s', '%s', '%d')"
query_comment_sql = "select * from comment WHERE `key` = '%s' ORDER BY `time` desc limit 10"
query_comment_below_sql = "select * from comment WHERE `key` = '%s' and `time` < '%d' order by `time` desc limit 10"
query_comment_id_sql = "select * from comment WHERE  id = '%d'"
query_comment_time_user_sql = "select * from comment WHERE time = '%d' and username = '%s'"
query_comment_key_count = "select count(*) from comment where `key` = '%s'"

insert_love_key_user = "insert into love (`key`, username) values ('%s', '%s')"
delete_love_key_user = "delete from love where `key` = '%s' and username = '%s'"
query_love_key_count = "select count(*) from love WHERE `key` = '%s'"
query_love_key_user = "select * from love WHERE `key` = '%s' and username = '%s' "


# article


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


# user


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


# comment


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


def get_comment_key_count(key):
    conn, cur = openDB()

    cur.execute(query_comment_key_count % key)
    result = cur.fetchone()[0]
    return result


# love


def insert_love(key, username, love):
    conn, cur = openDB()

    if love:
        cur.execute(query_love_key_user % (key, username))
        result = cur.fetchone()
        if result is None:
            cur.execute(insert_love_key_user % (key, username))
    else:
        cur.execute(delete_love_key_user % (key, username))
    conn.commit()

    cur.execute(query_love_key_user % (key, username))
    result = cur.fetchone()
    if result is None:
        result = False
    else:
        result = True
    closeDB(conn, cur)

    return result


def get_if_love(key, username):
    conn, cur = openDB()

    cur.execute(query_love_key_user % (key, username))
    result = cur.fetchone()

    if result is None:
        result = False
    else:
        result = True

    cur.execute(query_love_key_count % key)
    love_num = cur.fetchone()[0]

    cur.execute(query_comment_key_count % key)
    comment_num = cur.fetchone()[0]

    return result, love_num, comment_num


def get_love_key_count(key):
    conn, cur = openDB()

    cur.execute(query_love_key_count % key)
    result = cur.fetchone()[0]

    return result


def openDB():
    conn = pymysql.connect(host=host, user=username, passwd=password, db=db_name, charset='utf8mb4')
    cur = conn.cursor()
    return conn, cur


def closeDB(conn, cur):
    cur.close()
    conn.close()


if __name__ == "__main__":
    print(
        get_if_love('test', '')
    )
