import unittest
import json
import os,sys
from ddt import ddt,data

from request_pub import config
from request_pub import httpRequest
from request_pub import getAssert
from request_pub import getConsParams
from request_pub import getParams

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data
from public import log


@ddt
class ConsultationProcess2Test(unittest.TestCase):
    """正确性测试，状态变更"""
    def setUp(self):
        self.log = log.setLog()

    def test_statusSave1(self):
        '''saveStatus,正确性测试'''
        self.log.info('saveStatus,正确性测试')
        params=getParams.getParam_sendStatus(config.appDBConf,'saveStatus',config.primid01,'15')
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #单据状态变化
        #self.assertEqual(getAssert.getPrimStatus(config.appDBConf,config.primid01),'15','单据状态变为15')


    def test_statusSave2(self):
        '''saveStatus,只传必填项'''
        self.log.info('saveStatus,只传必填项')
        params=getParams.getParam_sendStatus(config.appDBConf,'saveStatus',config.primid01,'20','','',1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #self.assertEqual(getAssert.getPrimStatus(config.appDBConf,config.primid01),'20','单据状态变为20')
        #为了acceptReject，多变更一次状态，否则不能退回两次
        params=getParams.getParam_sendStatus(config.appDBConf,'saveStatus',config.primid01,'30','','',1)
        result=httpRequest.postRequest(config.app_url,params)


    def test_t_rejectSave1(self):
        ''' acceptReject,正确性测试'''
        self.log.info('acceptReject,正确性测试')
        params=getParams.getParam_reject(config.appDBConf,'acceptReject',config.primid01)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['message'],"请求成功")
        self.assertEqual(getAssert.getPrimStatus(config.appDBConf,config.primid01),'20','单据状态变为20')


    def test_t_rejectSave2(self):
        ''' acceptReject,只传必填项'''
        self.log.info('acceptReject,只传必填项')
        params=getParams.getParam_reject(config.appDBConf,'acceptReject',config.primid01,'','',1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['message'],"请求成功")
        self.assertEqual(getAssert.getPrimStatus(config.appDBConf,config.primid01),'15','单据状态变为15')

"""
    def test_statusSend1(self):
        ''' sendStatus:正确性测试'''
        self.log.info('sendStatus:正确性测试')

        params=getParams.getParam_sendStatus(config.consDBConf,'sendStatus','20180730005','20')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")

    @unittest.skip("test")
    def test_statusSend2(self):
        ''' sendStatus:只传必填项'''
        self.log.info('sendStatus:只传必填项')
        params=getParams.getParam_sendStatus(config.appDBConf,'sendStatus',config.primid1,'20','','',1)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")

    @unittest.skip("test")
    def test_t_rejectSend1(self):
        '''sendReject:正确性测试'''
        self.log.info('sendReject:正确性测试')
        params=getParams.getParam_reject(config.appDBConf,'sendReject',config.primid1)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")

    @unittest.skip("test")
    def test_t_rejectSend2(self):
        ''' sendReject:只传必填项'''
        self.log.info('sendReject:只传必填项')
        params=getParams.getParam_reject(config.appDBConf,'sendReject',config.primid03)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
"""
if __name__=="__main__":
    unittest.main(verbosity=2)
