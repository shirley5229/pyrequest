import unittest
import json
import os,sys
from ddt import ddt,data

from request_pub import config
from request_pub import httpRequest
from request_pub import getParams
from request_pub import getAssert

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data
from public import log

@ddt
class SendRejectTest(unittest.TestCase):
    """会诊医生，发起会诊退回"""
    def setUp(self):
        self.dbConfig = "applyOracleConf"
        self.logicName = "sendReject"
        self.log = log.setLog()

    @unittest.skip("test")
    def test_success(self):
        ''' 正常获取token'''
        self.log.info(self.logicName+':正确性测试')
        params=getParams.getParam_reject(self.dbConfig,self.logicName,config.primNo03)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")


    @data('id','opuserid','opusername')
    def test_null1(self,nullParam):
        ''' id传入null'''
        self.log.info(self.logicName+':必填项'+nullParam+'为空')
        params=getParams.getParam_reject(self.dbConfig,self.logicName,config.primNo4,nullParam)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['message'],"必填项为空",nullParam+"为空")


if __name__=="__main__":
    unittest.main(verbosity=2)
