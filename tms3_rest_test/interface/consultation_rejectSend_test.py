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
    """发起会诊退回,异常性测试"""
    def setUp(self):
        self.logicName = "sendReject"
        self.log = log.setLog()

    @data('id','opuserid')
    def test_null1(self,nullParam):
        ''' id传入null'''
        self.log.info(self.logicName+':必填项'+nullParam+'为空')
        params=getParams.getParam_reject(config.appDBConf,self.logicName,config.primid1,nullParam)
        result=httpRequest.postRequest(config.cons_url,params)
        if nullParam=='id':
            self.assertEqual(result['message'],"id为空，请传输id值")
        else:
            self.assertEqual(result['message'],"必填项为空")

    def test_error1(self):
        ''' 会诊id在申请端不存在'''
        self.log.info(self.logicName + ':会诊id在申请端不存在')
        params=getParams.getParam_reject(config.appDBConf,self.logicName,config.primid1,'','id')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual("根据id查询会诊失败" ,result['message'])

    def test_error2(self):
        '''会诊状态小于前质控,不予处理'''
        self.log.info(self.logicName + ':会诊状态小于前质控,不予处理')
        params=getParams.getParam_reject(config.appDBConf,self.logicName,config.primid1)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertTrue("会诊状态节点值小于前质控,暂不予处理" in result['message'])

if __name__=="__main__":
    unittest.main(verbosity=2)
