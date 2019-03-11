from redis_conn import local



def hello_world():
    return 'Hello World!'


def calculater(x, y):
    return x + y


def add_update_contact(conn, user, contact):
    ac_list = 'recent' + user
    pipeline = conn.pipeline(True)
    pipeline.lrem(ac_list, 0, contact)
    pipeline.lpush(ac_list, contact)
    pipeline.ltrim(ac_list, 0, 99)
    pipeline.execute()


def get_recent_contact(conn, user):
    act_list = 'recent' + user

    result = conn.lrange(act_list, 0, -1)

    return result


def fetch_autocomplete_list(conn, user, prefix):
    act_list = 'recent' + user

    results = conn.lrange(act_list, 0, -1)
    match = []
    for result in results:
        if result.lower().startswith(prefix):
            match.append(result)

    return match


if __name__ == '__main__':
    # va =hello_world()
    # result=calculater(1,2)
    con = local
    user = 'zhang'
    contact = 'you are so good'
    # add_update_contact(con,user,contact)
    # result=get_recent_contact(con,user)

    prefix = 'y'
    print(fetch_autocomplete_list(con, user, prefix))
