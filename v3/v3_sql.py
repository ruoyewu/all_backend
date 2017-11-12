import pymysql

from util import sql_util
import time


start_transaction = "START TRANSACTION"
transaction_commit = "COMMIT"

query_user_id = "select name from user WHERE id = '%d'"
query_user_name = "select * from user where name = '%s'"
insert_user_name_pass_time = "insert into user (name, password, create_time) values ('%s', '%s', '%d')"
update_user_read_sql = "update user set read_time = '%d'where id = '%d'"

insert_article_sql = "insert into article values('%s', '%s')"
query_article_sql = "select * from article WHERE `key`= '%s'"

insert_comment_sql = "insert into comment (time, userid, content, `key`, parent) values " \
                     "('%d', '%d', '%s', '%s', '%d')"
query_comment_sql = "select * from comment WHERE `key` = '%s' ORDER BY `time` desc limit 10"
query_comment_below_sql = "select * from comment WHERE `key` = '%s' and `time` < '%d' order by `time` desc limit 10"
query_comment_id_sql = "select * from comment WHERE  id = '%d'"
query_comment_time_user_sql = "select * from comment WHERE time = '%d' and userid = '%d'"
query_comment_key_count = "select count(*) from comment where `key` = '%s'"
query_comment_parent = "select * from comment where parent = '%d'"
delete_comment_id_sql = "delete from comment where id = '%d'"
query_comment_parent_user = "select * from comment where parent in (select id from comment where userid = '%d') order by `time` desc limit 10"
query_comment_parent_user_below = "select * from comment where parent in (select id from comment where userid = '%d') and `time` < '%d' order by `time` desc limit 10"
insert_comment_love = "insert into comment_love (comment_id, userid) values ('%d', '%d')"
delete_comment_love = "delete from comment_love where comment_id = '%d' and userid = '%d'"
query_comment_love_count = "select count(*) from comment_love where comment_id = '%d'"
query_comment_love_id_user = "select * from comment_love where comment_id = '%d' and userid = '%d'"

insert_love_key_user = "insert into love (`key`, userid) values ('%s', '%d')"
delete_love_key_user = "delete from love where `key` = '%s' and userid = '%d'"
query_love_key_count = "select count(*) from love WHERE `key` = '%s'"
query_love_key_user = "select * from love WHERE `key` = '%s' and userid = '%d'"

insert_favorite_sql = "insert into favorite (userid, info, `time`, `key`) values ('%d', '%s', '%d', '%s')"
query_favorite_sql = "select * from favorite where userid = '%d' order by `time` desc limit 10"
query_favorite_time_sql = "select * from favorite where userid = '%d' and `time` < '%d' order by `time` desc limit 10"
query_favorite_user_key_sql = "select * from favorite where userid = '%d' and `key` = '%s'"
delete_favorite_user_key = "delete from favorite where userid = '%d' and `key` = '%s'"


# user


def user_login(name, password):
    conn, cur = openDB()

    content = {}
    data = get_user_name(name, cur)
    if data == 'no':
        result = False
        info = "没有此用户"
    elif data[2] == password:
        result = True
        info = {'id': data[0], 'name': data[1]}
        content['read_time'] = data[3]
    else:
        result = False
        info = "密码错误"

    closeDB(conn, cur)

    return {
        'result': result,
        'info': info,
        'content': content
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
                t = time.time()
                t = int(t * 1000)
                cur.execute(insert_user_name_pass_time % (name, password, t))
                conn.commit()
            except:
                pass

            data = get_user_name(name, cur)
            if data == 'no':
                result = False
                info = "注册失败"
            else:
                result = True
                info = {'id': data[0], 'name': data[1]}
        else:
            result = False
            info = "用户名已存在"

    closeDB(conn, cur)
    return {
        'result': result,
        'info': info
    }


def user_read_time_update(time, userid):
    conn, cur = openDB()

    try:
        cur.execute(update_user_read_sql % (time, userid))
        result = True
        info = '上传成功'
    except:
        result = False
        info = "上传失败"

    closeDB(conn, cur)

    return {
        'result': result,
        'info': info
    }
    pass


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


def get_article_info(key, userid):
    conn, cur = openDB()

    cur.execute(query_love_key_user % (key, userid))
    result = cur.fetchone()

    if result is None:
        result = False
    else:
        result = True

    cur.execute(query_love_key_count % key)
    love_num = cur.fetchone()[0]

    cur.execute(query_comment_key_count % key)
    comment_num = cur.fetchone()[0]

    favorite = get_favorite_key_user(key, userid, cur)

    closeDB(conn, cur)

    return {
        'result': result,
        'love': love_num,
        'comment': comment_num,
        'favorite': favorite
    }


# favorite


def put_favorite(userid, time, info, key, favorite):
    conn, cur = openDB()

    if favorite == '0':
        cur.execute(delete_favorite_user_key % (userid, key))
    else:
        if get_favorite_key_user(key, userid, cur):
            pass
        else:
            cur.execute(insert_favorite_sql % (userid, info, time, key))
    conn.commit()

    result = get_favorite_key_user(key, userid, cur)

    closeDB(conn, cur)

    return {
        'result': result
    }


def get_favorite_time(userid, time):
    conn, cur = openDB()

    if time == 0:
        cur.execute(query_favorite_sql % userid)
    else:
        cur.execute(query_favorite_time_sql % (userid, time))

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


def get_comment_list(key, time, userid):
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
            comment_list.append(parseCommentData(item, cur, userid))

    closeDB(conn, cur)
    if len(comment_list) >= 10:
        next = comment_list[9]['time']
    else:
        next = -1

    return {
        'result': result,
        'info': info,
        'list': comment_list,
        'next': next
    }


def get_comment_list_parent(userid, time):
    conn, cur = openDB()

    if time == 0:
        cur.execute(query_comment_parent_user % userid)
    else:
        cur.execute(query_comment_parent_user_below % (userid, time))

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
            comment_list.append(parseCommentData(item, cur, userid))

    closeDB(conn, cur)
    if len(comment_list) >= 10:
        next = comment_list[-1]['time']
    else:
        next = -1

    return {
        'result': result,
        'info': info,
        'list': comment_list,
        'next': next
    }


def put_comment(key, time, userid, content, parent):
    conn, cur = openDB()

    try:
        cur.execute(insert_comment_sql % (time, userid, content, key, parent))
        conn.commit()
        result = 'ok'
    except:
        result = 'error'

    if result == 'ok':
        cur.execute(query_comment_time_user_sql % (time, userid))
        data = cur.fetchone()
        if data is None:
            result = False
            info = "评论失败"
        else:
            result = True
            info = parseCommentData(data, cur, userid)
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


def set_love(key, userid, love):
    conn, cur = openDB()

    if love == '0':
        cur.execute(delete_love_key_user % (key, userid))
    else:
        if get_love_key_user(key, userid, cur):
            pass
        else:
            cur.execute(insert_love_key_user % (key, userid))
    conn.commit()

    if get_love_key_user(key, userid, cur):
        result = True
    else:
        result = False

    closeDB(conn, cur)
    return {
        'result': result
    }


def set_comment_love(id, userid, love):
    conn, cur = openDB()

    if love == '0':
        cur.execute(delete_comment_love % (id, userid))
    else:
        if get_comment_love_id_user(id, userid, cur):
            pass
        else:
            cur.execute(insert_comment_love % (id, userid))
    conn.commit()

    if get_comment_love_id_user(id, userid, cur):
        result = True
    else:
        result = False

    closeDB(conn, cur)
    return {
        'result': result
    }

# private


def openDB():
    return sql_util.openDB()


def closeDB(conn, cur):
    sql_util.closeDB(conn, cur)


def parseCommentData(data, cur, user):
    id = data[0]
    time = data[1]
    userid = data[2]
    content = data[3]
    key = data[4]
    parent = data[5]
    if parent != 0:
        cur.execute(query_comment_id_sql % parent)
        p = cur.fetchone()
        if p is None:
            parent = ''
        else:
            parent = get_username(p[2], cur) + ' : ' + p[3]
    else:
        parent = ''

    cur.execute(query_comment_love_count % id)
    love = cur.fetchone()[0]
    is_love = get_comment_love_id_user(id, user, cur)

    return {
        'id': id,
        'time': time,
        'userid': userid,
        'username': get_username(userid, cur),
        'content': content,
        'key': key,
        'parent': parent,
        'love': love,
        'is_love': is_love
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


def get_love_key_user(key, userid, cur):
    cur.execute(query_love_key_user % (key, userid))
    result = cur.fetchone()

    if result is None:
        result = False
    else:
        result = True

    return result


def get_comment_love_id_user(id, userid, cur):
    cur.execute(query_comment_love_id_user % (id, userid))
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
    return result


def parseFavoriteData(data):
    userid = data[1]
    info = data[2]
    time = data[3]
    key = data[4]

    return {
        'userid': userid,
        'info': info,
        'time': time,
        'key': key
    }


def get_favorite_key_user(key, userid, cur):
    cur.execute(query_favorite_user_key_sql % (userid, key))
    data = cur.fetchone()
    if data is None:
        return False
    else:
        return True


def get_username(userid, cur):
    cur.execute(query_user_id % userid)
    data = cur.fetchone()
    if data is None:
        return 'no user'
    else:
        return data[0]


if __name__ == '__main__':
    print(
        get_comment_list_parent(2, 123456)
    )
