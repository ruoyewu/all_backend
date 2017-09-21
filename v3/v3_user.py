import json

from v3 import v3_sql


def register_user(name, pwd, email, phone):
    if len(name) < 1 or len(name) > 20:
        result = False
        info = '用户名长度错误'
    elif len(pwd) < 6 or len(pwd) > 50:
        result = False
        info = '密码长度错误'
    else:
        result = v3_sql.put_user(name, pwd, email, phone)
        if result == 'ok':
            result = True
            info = '注册用户成功'
        else:
            result = False
            info = '用户已存在'

    return result, info


def login_user(name, pwd):
    user = v3_sql.get_user({'id': -1, 'name': name})
    if user == 'no':
        result = False
        info = '无此用户'
    elif user[2] != pwd:
        result = False
        info = '密码错误'
    else:
        result = True
        info = '登录成功'

    return result, info


def logout_user(name):
    user = v3_sql.get_user({'id': -1, 'name': name})
    if user == 'no':
        result = False
        info = '无此用户'
    else:
        result = True
        info = '注销成功'

    return result, info


if __name__ == '__main__':
    result = register_user('dasd', 'fasdfasfda', '', '')
    print(json.dumps(result, ensure_ascii=False))
    pass


