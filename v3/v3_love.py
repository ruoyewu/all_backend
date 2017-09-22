from v3 import v3_sql


def get_article_info(key, username):
    result, love_n, comment_n = v3_sql.get_if_love(key, username)

    return {
        'result': result,
        'love': love_n,
        'comment': comment_n
    }


def set_article_love(key, username, love):
    if love == '0':
        love = False
    else:
        love = True

    result = v3_sql.insert_love(key, username, love)
    return {
        'result': result
    }


if __name__ == '__main__':
    print(
        get_article_info('', 'ruoye')
    )