from pymysql import *


class Mysqlhelp():
    connect_params = {
        'host': 'localhost',
        'user': 'root',
        'password': 'itcast',
        'db': 'mytestdb'
    }

    def __init__(self, connect_params):
        """
        初始化类属性
        :param connect_params:
        """
        self.__host = connect_params['host']
        self.__user = connect_params['user']
        self.__password = connect_params['password']
        self.__db = connect_params['db']

    def __connect(self):
        """
        创建数据库连接
        :return:
        """
        self.__connect = Connect(host=self.__host, user=self.__user, password=self.__password, database=self.__db)
        self.__cursor = self.__connect.cursor()

    def __colse(self):
        """
        关闭连接和游标
        :return:
        """
        self.__connect.close()
        self.__cursor.close()

    def get_one(self, sql, params):
        """
        获取单条数据
        :param sql:
        :param params:
        :return:
        """
        result = None
        try:
            self.__connect()
            self.__cursor.execute(sql, params)
            result = self.__cursor.fetchone()
            self.__connect.close()
        except Exception as e:
            raise e
        return result

    def get_all(self, sql, params):
        """
        获取所有数据
        :param sql:
        :param params:
        :return:
        """
        result = ()
        try:
            self.__connect()
            self.__cursor.execute(sql, params)
            result = self.__cursor.fetchall()
            self.__connect.close()
        except Exception as e:
            raise e
        return result

    def insert(self, sql, params):
        """
        插入数据
        :param sql:
        :param params:
        :return:
        """
        return self.__edit(sql, params)

    def insert_many(self, sql, params):
        result_list = []
        try:
            self.__connect()
            result_list = self.__cursor.executemany(sql, params)
            self.__connect.commit()
            self.__connect.close()
        except Exception as e:
            raise e
        return result_list

    def delete(self, sql, params):
        """
        删除数据
        :param sql:
        :param params:
        :return:
        """
        return self.__edit(sql, params)

    def update(self, sql, params):
        """
        更新数据
        :param sql:
        :param params:
        :return:
        """
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        count = 0
        try:
            self.__connect()
            count = self.__cursor.execute(sql, params)
            self.__connect.commit()
            self.__connect.close()

        except Exception as e:
            raise e
        return count
