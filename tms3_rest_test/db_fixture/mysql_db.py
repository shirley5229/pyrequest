import pymysql.cursors
import os
import configparser as cparser

#========读取 db_config.ini 文件=======
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf",'host')
port = cf.get("mysqlconf","port")
db = cf.get("mysqlconf","db_name")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")

#========Mysql基础操作=======
class DB:
    """Mysql基础操作."""
    def __init__(self):
        try:
            self.connection = pymysql.connect(host = host,user = user,password = password,
                db=db,charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error {0}:{1}".format(e.args[0],e.args[1]))

    def clear(self,table_name):
        '''清空表数据'''
        real_sql = "truncate table"+table_name+";"
        #real_sql = "delete from "+table_name+";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    def insert(self,table_name,table_data):
        '''插入数据'''
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        #示例：INSERT INTO Persons (LastName, Address) VALUES ('Wilson', 'Champs-Elysees')
        real_sql = "INSERT INTO "+table_name +"("+key+") VALUES("+value+")"
        #print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    def close(self):
        '''关闭连接'''
        self.connection.close()


if __name__=='__main__':
    db = DB()
    table_name = "sign_event"
    #ID自动生成
    data = {'name':'红米','status':1,
            'address':'国家舞台','start_time':'2018-04-13 00:25:42'}
    table_name2 = "sign_guest"
    #phone和event_id，唯一性约束
    data2 = {'realname':'Alen','phone':153535454,'email':'Alan@mail.com',
            'sign':0,'event_id':1}
    db.insert(table_name,data)
    db.insert(table_name2,data2)
    db.close()
