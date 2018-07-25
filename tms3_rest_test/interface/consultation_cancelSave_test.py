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

class CancelConsultationTest(unittest.TestCase):
    """会诊医生，接受取消会诊申请"""
    def setUp(self):
        self.dbConfig = "consOracleConf"   #从会诊端数据库获取数据
        self.logicName = "cancelConsultation"
        self.log = log.setLog()

    @unittest.skip("test")
    def test_a_success(self):
        ''' 传入正确的primid'''
        self.log.info(self.logicName+':正确性测试')
        params=getParams.getParam_cancelConsultation(self.dbConfig,self.logicName,config.primNo01)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #单据状态变为取消会诊=90
        self.assertEqual(getAssert.getPrimStatus(self.dbConfig,config.primNo01),'90','单据状态未变为取消')

    def test_null(self):
        ''' primid传入空'''
        self.log.info(self.logicName+':必填项primid为空')
        params=getParams.getParam_cancelConsultation(self.dbConfig,self.logicName,'','')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"16")
        self.assertEqual(result['message'],"id为空，请传输id值")

    def test_error1(self):
        ''' 传入错误的primid'''
        self.log.info(self.logicName+':传入错误的primid')
        params=getParams.getParam_cancelConsultation(self.dbConfig,self.logicName,'','1111112222')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"19")
        self.assertEqual(result['message'],"根据id查询会诊失败")

    def test_error2(self):
        ''' 传入已经是取消状态的primid'''
        self.log.info(self.logicName+':传入已经是取消状态的primid')
        params=getParams.getParam_cancelConsultation(self.dbConfig,self.logicName,config.primNo01)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"18")
        self.assertEqual(result['message'],"会诊状态非法")

if __name__=="__main__":
    unittest.main(verbosity=2)
