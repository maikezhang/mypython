from redis_conn import live_online
import json

def getliveDetailUserKeys():
    zookeyprex = 'live.CustomerVOCache.live_customer_vo_*'
    results = live_online.keys(zookeyprex)
    a=0
    for result in results:
        a=a+1
        print(result)
    print(a)
    return results

def getKeyTtl():
    key='live.CustomerVOCache.live_customer_vo_1494912'
    ttl=live_online.ttl(key)
    print(ttl)


def delBatch(keys):
    with live_online.pipeline() as pipe:
        for key in keys:
            pipe.delete(key)
        pipe.execute()


def delLiveDetailUserKey(key):
    print(live_online.delete(key))

if __name__=='__main__':
    getKeyTtl()
    # keys=getliveDetailUserKeys()
    a=0
    # for key in keys:
    #     a=a+1
    #     print(key)
    #     delLiveDetailUserKey(key)
    # print(a)
    # delBatch(keys)