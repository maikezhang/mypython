import redis

from config import localhost,live_dev,zoo_regress,zoo_online,redis_live_dev\
    ,redis_live_test,redis_live_online,redis_live_regress

local = redis.Redis(
    host=localhost['host'],
    port=localhost['port'],
    db=localhost['db']
)

live_dev_redis=redis.Redis(
    host=live_dev['host'],
    port=live_dev['port'],
    db=live_dev['db'],
    password=live_dev['password']
)

zoo_redis=redis.Redis(
    host=zoo_regress['host'],
    port=zoo_regress['port'],
    db=zoo_regress['db'],
    password=zoo_regress['password']
)

zoo_online_redis=redis.Redis(
    host=zoo_online['host'],
    port=zoo_online['port'],
    db=zoo_online['db'],
    password=zoo_online['password']
)

live_dev=redis.Redis(
    host=redis_live_dev['host'],
    port=redis_live_dev['port'],
    db=redis_live_dev['db'],
    password=redis_live_dev['password']
)

live_test=redis.Redis(
    host=redis_live_test['host'],
    port=redis_live_test['port'],
    db=redis_live_test['db'],
    password=redis_live_test['password']
)


live_online=redis.Redis(
    host=redis_live_online['host'],
    port=redis_live_online['port'],
    db=redis_live_online['db'],
    password=redis_live_online['password']
)


live_regress=redis.Redis(
    host=redis_live_regress['host'],
    port=redis_live_regress['port'],
    db=redis_live_regress['db'],
    password=redis_live_regress['password']
)