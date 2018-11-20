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
        self.base_url = "http://httpbin.org/get"

    def test_add_event_all_null(self):
        '''所有参数为空''' 
        payload={'eid':'','name':'','status':1,'address':'','start_time':''}
        r = requests.post(self.base_url,data=payload)
        print(r)
        result=r.json()
        print(result)
        self.assertEqual(result['status'],'10021')
        self.assertEqual(result['message'],'parameter error.')

    def test_add_event_name_exist(self):
        '''名称已经存在'''
        payload={'name':'红米Pro发布会','status':1,'address':'北京水立方','start_time':'20180502'}
        r=requests.post(self.base_url,data=payload)
        result = r.json( )
        print(http://httpbin.org/getresult)
        self.assertEqual(result['status'],10023)
        self.assertEqual(result['message'],'event name already exists.')



if __name__=="__main__":
    unittest.main()
