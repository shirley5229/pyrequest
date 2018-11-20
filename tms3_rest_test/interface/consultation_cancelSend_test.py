import unittest
import json
import os,sys

from request_pub import config
from request_pub import httpRequest
from request_pub import getParams
from request_pub import getAssert

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data
from public import log

class SendCancelConsultationTest(unittest.TestCase):
    """发起取消会诊,异常性测试"""
    @classmethod
    def setUpClass(self):
        self.logicName = "sendCancelConsultation"
        self.log = log.setLog()

    def test_error2(self):
        ''' 传入已经是取消状态的primid'''
        self.log.info(self.logicName+':传入已经是取消状态的primid')
        params=getParams.getParam_cancelConsultation(config.appDBConf,self.logicName,config.primid5)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"18")
        self.assertEqual(result['message'],"会诊状态非法")

    def test_null(self):
        ''' primid传入空'''
        self.log.info(self.logicName+':必填项primid为空')
        params=getParams.getParam_cancelConsultation(config.appDBConf,self.logicName,'','')
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"16")
        self.assertEqual(result['message'],"id为空，请传输id值")

    def test_error1(self):
        ''' 传入错误的primid'''
        self.log.info(self.logicName+':传入错误的primid')
        params=getParams.getParam_cancelConsultation(config.appDBConf,self.logicName,'','1111112222')
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"19")
        self.assertEqual(result['message'],"根据id查询会诊失败")



if __name__=="__main__":
    unittest.main(verbosity=2)
