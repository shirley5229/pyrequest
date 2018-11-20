import sys
sys.path.append('../db_fixture')
from .mysql_db import DB

#创建数据
datas = {
    'sign_event':[{'id':1,'name':'红米Pro发布会','status':1,
                'address':'北京展会中心','start_time':'2018-04-01 14:00:00'},
                {'id':2,'name':'可参加人数为0','status':1,
                            'address':'北京展会中心','start_time':'2018-05-01 14:00:00'},
                {'id':3,'name':'发布会为失效状态','status':0,
                            'address':'北京展会中心','start_time':'2018-06-01 14:00:00'},
                {'id':4,'name':'发布会已结束','status':1,
                            'address':'北京展会中心','start_time':'2018-03-01 14:00:00'},
                {'id':5,'name':'苹果MAC发布会','status':1,
                            'address':'北京展会中心','start_time':'2018-04-12 14:00:00'},
                ],
    'sign_guest':[{'id':1,'realname':'Alen','phone':1350001,'email':'Alen@mail.com',
                'sign':0,'event_id':1},
                {'id':2,'realname':'has sign','phone':1350002,'email':'Alen@mail.com',
                            'sign':1,'event_id':1},
                {'id':3,'realname':'tom','phone':1350003,'email':'Alen@mail.com',
                            'sign':0,'event_id':5},
                ],
}

def init_data():
    db=DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()

if __name__=='__main__':
    init_data()
