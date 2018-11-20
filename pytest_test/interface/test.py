import unittest
import requests
import os,sys
import timeout_decorator

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

if __name__=="__main__":
    unittest.main()
