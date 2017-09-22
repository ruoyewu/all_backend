from v3 import v3_sql


def get_comment(key, below):
    comment_list = []
    list = v3_sql.get_comment(key, below)
    if len(list) == 0:
        result = True
        info = '没有更多了'
    else:
        result = True
        info = '获取成功'
        for i in range(len(list)):
            item = list[i]
            comment_list.append(parseData(item))

    if len(comment_list) > 0:
        next = comment_list[len(comment_list) - 1]['time']
    else:
        next = -1

    return {
        'result': result,
        'info': info,
        'list': comment_list,
        'next': next
    }


def add_comment(key, time, username, content, parent):
    result = v3_sql.put_comment(time, username, content, key, parent)
    if result == 'ok':
        result = True
        data = v3_sql.get_comment_time_username(time, username)
        if data == 'no':
            info = '评论失败'
            result = False
        else:
            info = parseData(data)
    else:
        result = False
        info = '评论失败'

    return {
        'result': result,
        'info': info
    }


def parseData(data):
    id = data[0]
    time = data[1]
    username = data[2]
    content = data[3]
    key = data[4]
    parent = data[5]
    if parent != 0:
        p = v3_sql.get_comment_id(parent)
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


if __name__ == '__main__':
    print(add_comment('test', 1234567, 'ruoye', 'ruoye', 0))