import pymysql

host = 'localhost'
username = 'root'
password = 'ILYT3421'
db_name = 'allapp'

start_transaction = "START TRANSACTION"
transaction_commit = "COMMIT"

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
query_comment_parent = "select * from comment where parent = '%d'"
delete_comment_id_sql = "delete from comment where id = '%d'"

insert_love_key_user = "insert into love (`key`, username) values ('%s', '%s')"
delete_love_key_user = "delete from love where `key` = '%s' and username = '%s'"
query_love_key_count = "select count(*) from love WHERE `key` = '%s'"
query_love_key_user = "select * from love WHERE `key` = '%s' and username = '%s'"


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


def get_article(key):
    conn, cur = openDB()
    try:
        cur.execute(query_article_sql % key)
        result = cur.fetchone()[1]
    except:
        result = 'no'

    closeDB(conn, cur)
    return result


def get_article_info(key, username):
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

    closeDB(conn, cur)

    return {
        'result': result,
        'love': love_num,
        'comment': comment_num
    }


# comment


def get_comment_list(key, time):
    conn, cur = openDB()

    if time == 0:
        cur.execute(query_comment_sql % key)
    else:
        cur.execute(query_comment_below_sql % (key, time))

    comment_list = []
    list = cur.fetchall()
    if len(list) == 0:
        result = True
        info = "没有更多了"
    else:
        result = True
        info = "获取更多"
        for i in range(len(list)):
            item = list[i]
            comment_list.append(parseCommentData(item, cur))

    closeDB(conn, cur)
    if len(comment_list) >=10:
        next = comment_list[9]['time']
    else:
        next = -1

    return {
        'result': result,
        'info': info,
        'list': comment_list,
        'next': next
    }


def put_comment(key, time, username, content, parent):
    conn, cur = openDB()

    try:
        cur.execute(insert_comment_sql % (time, username, content, key, parent))
        conn.commit()
        result = 'ok'
    except:
        result = 'error'

    if result == 'ok':
        cur.execute(query_comment_time_user_sql % (time, username))
        data = cur.fetchone()
        if data is None:
            result = False
            info = "评论失败"
        else:
            result = True
            info = parseCommentData(data, cur)
    else:
        result = False
        info = '评论失败'

    return {
        'result': result,
        'info': info
    }


def delete_comment(id):
    conn, cur = openDB()

    try:
        cur.execute(start_transaction)
        delete_comment_id(id, cur)
        cur.execute(transaction_commit)
        result = True
    except:
        result = False

    closeDB(conn, cur)
    return result


# love


def set_love(key, username, love):
    conn, cur = openDB()

    if love == '0':
        cur.execute(delete_love_key_user % (key, username))
    else:
        if get_love_key_user(key, username, cur):
            pass
        else:
            cur.execute(insert_love_key_user % (key, username))
    conn.commit()

    if get_love_key_user(key, username, cur):
        result = True
    else:
        result = False

    closeDB(conn, cur)
    return {
        'result': result
    }


# private


def openDB():
    conn = pymysql.connect(host=host, user=username, passwd=password, db=db_name, charset='utf8mb4')
    cur = conn.cursor()
    return conn, cur


def closeDB(conn, cur):
    cur.close()
    conn.close()


def parseCommentData(data, cur):
    id = data[0]
    time = data[1]
    username = data[2]
    content = data[3]
    key = data[4]
    parent = data[5]
    if parent != 0:
        cur.execute(query_comment_id_sql % id)
        p = cur.fetchone()
        if p is None:
            parent = ''
        else:
            parent = p[2] + ' : ' + p[3]
    else:
        parent = ''

    return {
        'id': id,
        'time': time,
        'username': username,
        'content': content,
        'key': key,
        'parent': parent
    }


def delete_comment_id(id, cur):
    children = get_comment_parent(id, cur)

    cur.execute(delete_comment_id_sql % id)

    for i in range(len(children)):
        delete_comment_id(children[i], cur)


def get_comment_parent(parent, cur):
    cur.execute(query_comment_parent % parent)

    id_list = []
    list = cur.fetchall()
    for i in range(len(list)):
        id_list.append(list[i][0])

    return id_list


def get_love_key_user(key, username, cur):
    cur.execute(query_love_key_user % (key, username))
    result = cur.fetchone()

    if result is None:
        result = False
    else:
        result = True

    return result


if __name__ == '__main__':
    print(
        get_article_info('test', 'r')
    )
