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
    """接收会诊退回,异常性测试"""
    @classmethod
    def setUpClass(self):
        self.logicName = "acceptReject"
        self.log = log.setLog()


    @data('id','opuserid')
    def test_null1(self,nullParam):
        ''' 必填项传入null'''
        self.log.info(self.logicName+':必填项'+nullParam+'为空')
        params=getParams.getParam_reject(config.appDBConf,"acceptReject",config.primid01,nullParam)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['message'],"必填项为空")

    def test_error1(self):
        ''' 会诊id在申请端不存在'''
        self.log.info(self.logicName + ':会诊id在申请端不存在')
        params=getParams.getParam_reject(config.appDBConf,"acceptReject",config.primid01,'','id')
        result=httpRequest.postRequest(config.app_url,params)
        self.assertTrue("会诊不存在,根据会诊id未查询到返回信息" in result['message'])

    def test_error2(self):
        '''会诊状态小于前质控,不予处理'''
        self.log.info(self.logicName + ':会诊状态小于前质控,不予处理')
        params=getParams.getParam_reject(config.appDBConf,"acceptReject",config.primid01)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertTrue("会诊状态节点值小于前质控,暂不予处理" in result['message'])

if __name__=="__main__":
    unittest.main(verbosity=2)
