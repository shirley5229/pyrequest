import unittest
import json
import os,sys
from ddt import ddt,data

from request_pub import config
from request_pub import httpRequest
from request_pub import getConsParams
from request_pub import getAssert

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data
from public import log

@ddt
class SendConsultationTest(unittest.TestCase):
    """发起会诊申请,异常性测试"""
    def setUp(self):
        self.logicName = "sendConsultation"
        self.log = log.setLog()

    @unittest.skip("由于工作流问题，无法测试")
    def test_success3(self):
        '''重复发送会诊'''
        self.log.info(self.logicName+':重复发送会诊')
        params = getConsParams.getParam(config.appDBConf,self.logicName,config.primid1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"200")
        self.assertEqual(result['message'],"{\"code\":null,\"message\":\"请勿重复发送会诊！\",\"datas\":null}")


    #异常测试，使用Excel
    @unittest.skip("异常不进行测试")
    @data(1,2,3,4,5,6,7,8,9,10,11,12)
    def test_null(self,rowNum):
        '''patientname传入空'''
        self.log.info(self.logicName+':传入空')
        #调用Excel中数据
        params = getConsParams.getParam(config.appDBConf,self.logicName,'',0,0,0,rowNum)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"05")
        self.assertEqual(result['message'],"必填项为空")

    def test_null1(self):
        '''primid传入空'''
        self.log.info(self.logicName+':primid传入空')
        params = getConsParams.getParam(config.appDBConf,self.logicName,config.primid2,0,0,0,0,'primid')
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"05")
        self.assertEqual(result['message'],"必填项为空")

    def test_null2(self):
        '''会诊科室id为空'''
        self.log.info(self.logicName+':会诊科室id为空')
        params = getConsParams.getParam(config.appDBConf,self.logicName,config.primid2,0,0,0,0,'assigndepartmentid')
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],'200')
        #{'message': '{"code":null,"message":"会诊科室id为空！","datas":null}', 'code': '200', 'datas': None}
        message=json.loads(result['message'])
        self.assertEqual(message['message'],"会诊科室id为空！")

if __name__=="__main__":
    unittest.main(verbosity=2)
