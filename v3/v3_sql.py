import pymysql

host = 'localhost'
username = 'root'
password = 'ILYT3421'
db_name = 'allapp'

start_transaction = "START TRANSACTION"
transaction_commit = "COMMIT"

query_user_name = "select * from user where name = '%s'"
insert_user_name_pass = "insert into user (name, password) values ('%s', '%s')"

insert_article_sql = "insert into article values('%s', '%s')"
query_article_sql = "select * from article WHERE `key`= '%s'"

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

insert_favorite_sql = "insert into favorite (username, info, `time`, `key`) values ('%s', '%s', '%d', '%s')"
query_favorite_sql = "select * from favorite where username = '%s' order by `time` desc limit 10"
query_favorite_time_sql = "select * from favorite where username = '%s' and `time` < '%d' order by `time` desc limit 10"
query_favorite_user_key_sql = "select * from favorite where username = '%s' and `key` = '%s'"
delete_favorite_user_key = "delete from favorite where username = '%s' and `key` = '%s'"


# user


def user_login(name, password):
    conn, cur = openDB()

    data = get_user_name(name, cur)
    if data == 'no':
        result = False
        info = "没有此用户"
    elif data == password:
        result = True
        info = name
    else:
        result = False
        info = "密码错误"

    closeDB(conn, cur)

    return {
        'result': result,
        'info': info
    }


def user_sign(name, password):
    conn, cur = openDB()
    if len(name) < 2:
        result = False
        info = "用户名长度应大于1"
    elif len(name) > 10:
        result = False
        info = "用户名长度应小于10"
    elif len(password) < 6:
        result = False
        info = "密码长度应大于5"
    elif len(password) > 30:
        result = False
        info = "密码长度应小于30"
    else:
        data = get_user_name(name, cur)
        if data == 'no':
            try:
                cur.execute(insert_user_name_pass % (name, password))
                conn.commit()
            except:
                pass

            data = get_user_name(name, cur)
            if data == 'no':
                result = False
                info = "注册失败"
            else:
                result = True
                info = name
        else:
            result = False
            info = "用户名已存在"

    closeDB(conn, cur)
    return {
        'result': result,
        'info': info
    }


# article


def put_article(key, content):
    conn, cur = openDB()
    try:
        cur.execute(insert_article_sql % (key, pymysql.escape_string(content)))
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

    favorite = get_favorite_key_user(key, username, cur)

    closeDB(conn, cur)

    return {
        'result': result,
        'love': love_num,
        'comment': comment_num,
        'favorite': favorite
    }


# favorite


def put_favorite(username, time, info, key, favorite):
    conn, cur = openDB()

    if favorite == '0':
        cur.execute(delete_favorite_user_key % (username, key))
    else:
        if get_favorite_key_user(key, username, cur):
            pass
        else:
            cur.execute(insert_favorite_sql % (username, info, time, key))
    conn.commit()

    result = get_favorite_key_user(key, username, cur)

    closeDB(conn, cur)

    return {
        'result': result
    }


def get_favorite_time(username, time):
    conn, cur = openDB()

    if time == 0:
        cur.execute(query_favorite_sql % username)
    else:
        cur.execute(query_favorite_time_sql % (username, time))

    favorite_list = []
    list = cur.fetchall()
    if len(list) == 0:
        result = True
    else:
        result = True
        for i in range(len(list)):
            item = list[i]
            favorite_list.append(parseFavoriteData(item))

    closeDB(conn, cur)

    if len(favorite_list) >= 10:
        next = favorite_list[9]['time']
    else:
        next = -1

    return {
        'result': result,
        'info': favorite_list,
        'next': next
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
    return {
        'result': result
    }


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
        cur.execute(query_comment_id_sql % parent)
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


def get_user_name(name, cur):
    cur.execute(query_user_name % name)
    result = cur.fetchone()
    if result is None:
        result = 'no'
    else:
        result = result[1]
    return result


def parseFavoriteData(data):
    username = data[0]
    info = data[1]
    time = data[2]
    key = data[3]

    return {
        'username': username,
        'info': info,
        'time': time,
        'key': key
    }


def get_favorite_key_user(key, username, cur):
    cur.execute(query_favorite_user_key_sql % (username, key))
    data = cur.fetchone()
    if data is None:
        return False
    else:
        return True


if __name__ == '__main__':
    print(
        get_favorite_time('ruoye', 12345657)
    )
