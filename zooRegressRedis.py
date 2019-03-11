from redis_conn import zoo_redis, zoo_online_redis
import json

def getZooCacheKeys():
    zookeyprex = 'zoo_new_cache*'
    results = zoo_redis.keys(zookeyprex)
    return results


def delZooCacheKeys(keys):
    print(zoo_redis.delete(keys))


def delBatch(keys):
    zoo_redis.pipeline()


def getVipUserEffects():
    results = zoo_online_redis.hgetall("zoo_vip_user_effects_on_off")
    print(results)
    # vipMap =json.loads(results)
    # print(vipMap)
    for result in results:

        print(zoo_online_redis.hget("zoo_vip_user_effects_on_off",result))



if __name__ == '__main__':
    getVipUserEffects()
