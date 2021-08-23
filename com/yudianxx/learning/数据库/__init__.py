#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql


class MysqlOperation():

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.open()

    def open(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'db': 'mytest',
            'user': 'root',
            'passwd': 'root',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor
        }
        conn = pymysql.connect(**config)
        self.conn = conn
        conn.autocommit(1)
        self.cursor = conn.cursor()

    def executeSQL(self, sql):
        print("excute sql -->>>\n", sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            print("result-->>\n", results)
            return results
        except:
            self.conn.rollback()



        finally:
            self.__exit__()

    def __exit__(self):
        '''退出时关闭游标关闭连接'''
        self.cursor.close()
        self.conn.close()

    def update(self):
        pass
