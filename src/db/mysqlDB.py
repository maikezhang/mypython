#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymysql


class mysqlDB(object):
    con = None
    cursor = None

    def __init__(self):
        self.con = pymysql.connect(
            host='172.16.8.8',
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

    def update(self,sql,params):
        dataresult=self.cursor.executemany(sql,params)
        self.con.commit()
        return dataresult

    def close(self):
        self.cursor.close()
        self.con.close()
        return
