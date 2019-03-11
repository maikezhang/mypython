from src.db.mysqlDB import mysqlDB


def getLivePlayBack():
    sql = "select * from live_playback order by id desc limit 1000 offset 4500"
    db_cursor = mysqlDB()
    datas = db_cursor.select(sql)
    db_cursor.close()
    dict = {}
    for data in datas:
        url = data[2]
        fileid = url.split('/')[4]
        # print(fileid)
        fileid = fileid[8:]
        # print(fileid)
        dict[data[0]] = fileid
    print(dict)

    return dict


def updateLivePlayBackFileId(dict):
    db_cursor = mysqlDB()
    sql=''
    array=[]
    for key in dict:
        tup1=(dict[key],key)
        array.append(tup1)
    print(array)

    sql="UPDATE live_playback set file_id=%s where id=%s"
    try:
        datas = db_cursor.update(sql,array)
    except Exception as e:
        print(e)
    db_cursor.close()

if __name__ == '__main__':
    dict=getLivePlayBack()
    updateLivePlayBackFileId(dict)
