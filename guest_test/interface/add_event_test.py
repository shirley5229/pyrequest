import unittest
import requests
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
    """添加发布会."""
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def test_add_event_all_null(self):
        '''所有参数为空'''
        payload={'eid':'','name':'','status':1,'address':'','start_time':''}
        r = requests.post(self.base_url,data=payload)
        result=r.json()
        print(result)
        self.assertEqual(result['status'],'10021')
        self.assertEqual(result['message'],'parameter error.')

    def test_add_event_name_exist(self):
        '''名称已经存在'''
        payload={'name':'红米Pro发布会','status':1,'address':'北京水立方','start_time':'20180502'}
        r=requests.post(self.base_url,data=payload)
        result = r.json( )
        print(result)
        self.assertEqual(result['status'],10023)
        self.assertEqual(result['message'],'event name already exists.')

    def test_add_event_dataType_error(self):
        '''日期格式错误'''
        payload={'name':'红米Pro发布会','status':1,'address':'北京水立方','start_time':'2018'}
        r=requests.post(self.base_url,data=payload)
        result = r.json( )
        print(result)
        self.assertEqual(result['status'],10024)
        self.assertEqual(result['message'],'event name already exists.')

    def test_add_event_success(self):
        '''添加成功'''
        payload={'name':'苹果发布会','status':1,'address':'纽约大厦','start_time':'20180902 12:00:00'}
        r=requests.post(self.base_url,data=payload)
        result = r.json()
        print(result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'add event success.')

if __name__=="__main__":
    test_data.init_data()
    unittest.main()
