

from src.db.mysqlDB import mysqlDB

from config import live_dev


if __name__ =='__main__':
    sql="select * from live_playback limit 10"
    db_cursor=mysqlDB()
    datas=db_cursor.select(sql)
    for data in datas:
        print(data[0])

    db_cursor.close()



