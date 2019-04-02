import unittest
import os,sys

from request_pub import config
from request_pub import httpRequest

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from public import log

@unittest.skip("logicName为空或错误的问题暂时不考虑")
class LogicNameTest(unittest.TestCase):
    """logicName测试"""

    @classmethod
    def setUpClass(self):
        self.log = log.setLog()

    def test_fail1(self):
        '''token地址的logicName错误'''
        self.log.info('token地址的logicName错误')
        params={'logicName':'crea1112222','token':'','messageId':'1','datas':{'platform_id':'6f9f10185dcf490f9916dec4687bc3fb'}}
        result=httpRequest.postRequest(config.token_url,params)
        self.assertEqual(result['code'],'07')
        self.assertEqual(result['message'],"服务名没有找到")

    def test_fail2(self):
        '''dataSynApi地址的logicName错误'''
        self.log.info('dataSynApi地址的logicName错误')
        params={'logicName':'crea1112222','token':'','messageId':'1','datas':{'platform_id':'6f9f10185dcf490f9916dec4687bc3fb'}}
        result=httpRequest.postRequest(config.appdata_url,params)
        self.assertEqual(result['code'],'07')
        self.assertEqual(result['message'],"服务名没有找到")

    def test_fail3(self):
        '''api地址的logicName错误'''
        self.log.info( 'api地址的logicName错误')
        params={'LOGICNAME':'crea1112222','TOKEN':'','MESSAGEID':'1','DATAS':{'id':'6f9f10185dcf490f9916dec4687bc3fb'}}
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],'07')
        self.assertEqual(result['message'],"服务名没有找到")

    def test_null1(self):
        '''token地址的logicName为空'''
        self.log.info('token地址的logicName为空')
        params={'logicName':'','token':'','messageId':'1','datas':{'platform_id':'6f9f10185dcf490f9916dec4687bc3fb'}}
        result=httpRequest.postRequest(config.token_url,params)
        self.assertEqual(result['code'],'07')
        self.assertEqual(result['message'],"服务名没有找到")

    def test_null2(self):
        '''dataSynApi地址的logicName为空'''
        self.log.info('dataSynApi地址的logicName为空')
        params={'logicName':'','token':'','messageId':'1','datas':{'platform_id':'6f9f10185dcf490f9916dec4687bc3fb'}}
        result=httpRequest.postRequest(config.appdata_url,params)
        self.assertEqual(result['code'],'07')
        self.assertEqual(result['message'],"服务名没有找到")

    def test_null3(self):
        '''api地址的logicName为空'''
        self.log.info( 'api地址的logicName为空')
        params={'LOGICNAME':'','TOKEN':'','MESSAGEID':'1','DATAS':{'id':'6f9f10185dcf490f9916dec4687bc3fb'}}
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],'07')
        self.assertEqual(result['message'],"服务名没有找到")


if __name__=="__main__":
    unittest.main(verbosity=2)
