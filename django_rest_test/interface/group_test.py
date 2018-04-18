import unittest
import requests

class GroupTest(unittest.TestCase):
    """Group查询测试"""
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/groups"

    def test_group1(self):
        ''' '''
        r = requests.get(self.base_url+'/1/',auth=('admin','django123'))
        result=r.json()
        print(result)
        self.assertEqual(result['name'],'test')




if __name__=="__main__":
    unittest.main()
