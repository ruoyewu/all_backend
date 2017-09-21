from v3 import v3_sql


def get_comment(key, below):
    comment_list = []
    list = v3_sql.get_comment(key, below)
    if len(list) == 0:
        result = False
        info = '没有更多了'
    else:
        result = True
        info = '获取成功'
        for i in range(len(list)):
            item = list[i]
            comment_list.append({
                'id': item[0],
                'time': item[1],
                'username': item[2],
                'content': item[3],
                'key': item[4],
                'parent': item[5]
            })

    return result, info, comment_list


def add_comment(key, time, username, content, parent):
    result = v3_sql.put_comment(time, username, content, key, parent)
    if result == 'ok':
        result = True
        info = '评论成功'
    else:
        result = False
        info = '评论失败'

    return result, info


if __name__ == '__main__':
    print(add_comment('test', 1234567, 'ruoye', 'ruoye', 0))