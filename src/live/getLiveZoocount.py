# -*- coding: utf-8 -*-
import pymysql
import redis


class mysqlDB_kaipao(object):
    con = None
    cursor = None

    def __init__(self):
        self.con = pymysql.connect(
            host='172.16.8.225',
            port=3306,
            user='app_live',
            db='kaipao',
            passwd='liveTfZkB9XLAMHN',
            charset='utf8'
        )

        self.cursor = self.con.cursor()

    def select(self, query):
        self.cursor.execute(query)
        dataresult = self.cursor.fetchall()

        return dataresult

    def close(self):
        self.cursor.close()
        self.con.close()
        return


class mysqlDB_zoo(object):
    con = None
    cursor = None

    def __init__(self):
        self.con = pymysql.connect(
            host='172.16.8.220',
            port=3306,
            user='app_zoo',
            db='zoo',
            passwd='zooW2iJQGPcUJ78',
            charset='utf8'
        )

        self.cursor = self.con.cursor()

    def select(self, query):
        self.cursor.execute(query)
        dataresult = self.cursor.fetchall()

        return dataresult

    def close(self):
        self.cursor.close()
        self.con.close()
        return


zoo_online_redis = redis.Redis(
    host='172.16.8.232',
    port=6380,
    db=5,
    password='8ed4d756495de0180ec2e1b72e0b894e'
)


def getRealCount():
    dblives = getlivelist()
    zids=dblives['zidData']

    dict = {}
    for dblive in dblives:
        relcount = getZooCacheKeys(dblive[1]).decode()
        totalmessage = getTotalMessage(dblive[1])
        dict[str(dblive[0])] = [dblive[1], relcount, totalmessage[0][1]]

    print(dict)
    return


# 获取聊天室的真实在线人数
def getZooCacheKeys(zids):

    dict=[]
    list=dict
    with zoo_online_redis.pipeline(transaction=False) as pipe:
        for i in zids:
            realc=pipe.get('zoo_dynamic_user_st_' + str(i))
            list.append(realc)
        results = pipe.execute()

    print(list)
    # zookeyprex = 'zoo_dynamic_user_st_' + str(zid)
    # results = zoo_online_redis.get(zookeyprex)
    return results


# 获取聊天室的累计发言次数
def getTotalMessage(zid):
    zids=tuple(zid)

    sql = 'select zid,count(zid) count from zoo.zoo_message where zid in ' + str(
        zids) + ' and type=0  GROUP BY zid '
    db_cursor = mysqlDB_zoo()
    zoo_data = db_cursor.select(sql)
    db_cursor.close()
    return zoo_data


# 获取正在的直播
def getlivelist():
    sql = "select id,zid from live_show where state=2 and status=0 and online=1"
    db_cursor = mysqlDB_kaipao()
    datas = db_cursor.select(sql)

    db_cursor.close()

    dicts = {}
    dicts['data']=datas
    array=[]
    list=array
    i=0
    for data in datas:
        list.append(data[1])
        i=i+1
    dicts['zidData']=list
    return dicts


if __name__ == '__main__':
    # getRealCount()
    # getTotalMessage(398438)
    dicts=getlivelist()
    zids=dicts['zidData']
    # zidCount=getTotalMessage(zids)
    # print(zidCount)
    realCount=getZooCacheKeys(zids)
    print(realCount)

