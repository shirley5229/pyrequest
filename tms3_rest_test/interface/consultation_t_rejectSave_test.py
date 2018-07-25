import unittest
import json
import os,sys
import time,datetime
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
class AcceptRejectTest(unittest.TestCase):
    """申请医生，接收会诊退回"""
    def setUp(self):
        self.dbConfig = "applyOracleConf"  #从会诊端数据库获取数据
        self.logicName = "acceptReject"
        self.log = log.setLog()

    @unittest.skip("test")
    def test_success(self):
        ''' 正常获取token'''
        self.log.info(self.logicName+':正确性测试')
        params=getParams.getParam_reject(self.dbConfig,self.logicName,config.primNo2)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['message'],"请求成功")
        #单据状态变为
        #self.assertEqual(getAssert.getPrimStatus(self.dbConfig,self.logicName,config.primNo2),1,'附件没有同步成功!')


    @data('id','opuserid','opusername')
    def test_null1(self,nullParam):
        ''' 必填项传入null'''
        self.log.info(self.logicName+':必填项'+nullParam+'为空')
        params=getParams.getParam_reject(self.dbConfig,self.logicName,config.primNo2,nullParam)
        result=httpRequest.postRequest(config.cons_url,params)
        if result=='id':
            self.assertEqual(result['message'],"id为空，请传输id值",nullParam+"为空")
        else:
            self.assertEqual(result['message'],"id为空，请传输id值",nullParam+"为空")

if __name__=="__main__":
    unittest.main(verbosity=2)
