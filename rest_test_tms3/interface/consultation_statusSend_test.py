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
class SendStatusTest(unittest.TestCase):
    """发出会诊状态,异常性测试"""
    @classmethod
    def setUpClass(self):
        self.logicName = "sendStatus"
        self.log = log.setLog()

    @data('id','status')
    def test_null(self,nullParam):
        '''必填项传入空'''
        self.log.info(self.logicName+':必填项传入空')
        params=getParams.getParam_sendStatus(config.appDBConf,self.logicName,config.primid3,"20",nullParam)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"05")
        self.assertEqual(result['message'],"必填项为空",nullParam+"为空")

    def test_error1(self):
        ''' ID在接收端不存在'''
        self.log.info(self.logicName+':ID在接收端不存在')
        params=getParams.getParam_sendStatus(config.appDBConf,self.logicName,config.primid2,"20","","111222")
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"19")
        self.assertEqual(result['message'],"根据id查询会诊失败")


if __name__=="__main__":
    unittest.main(verbosity=2)
