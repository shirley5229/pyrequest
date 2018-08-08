import unittest
import json
import os,sys

from request_pub import config
from request_pub import httpRequest
from request_pub import getParams

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data
from public import log

class GetConsultationReportTest(unittest.TestCase):
    """接受会诊报告获取,异常性测试"""
    def setUp(self):
        self.dbConfig = "consOracleConf"
        self.logicName = "getConsultationReport"
        self.log = log.setLog()


    def test_getReport(self):
        ''' 正确性测试'''
        self.log.info(self.logicName+':正确性测试')
        params=getParams.getParam_getReport(self.dbConfig,self.logicName,config.primid05)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],'00')
        self.assertEqual(result['message'],"请求成功")
        #获取报告列表
        list= result['datas']['list']
        self.assertTrue(len(list)>0,'报告为空')


    def test_null(self):
        ''' id传入空'''
        self.log.info(self.logicName+':id传入空')
        params=getParams.getParam_getReport(self.dbConfig,self.logicName,'','')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],'05')
        self.assertEqual(result['message'],"必填项为空")


    def test_error1(self):
        ''' id不存在'''
        self.log.info(self.logicName+':id不存在')
        params=getParams.getParam_getReport(self.dbConfig,self.logicName,'','errorid')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],'12')
        self.assertEqual(result['message'],"主数据信息异常")


    def test_error2(self):
        ''' 报告不存在'''
        self.log.info(self.logicName+':报告不存在')
        params=getParams.getParam_getReport(self.dbConfig,self.logicName,config.primid04)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['message'],"没有查询到报告数据！")

if __name__=="__main__":
    unittest.main(verbosity=2)
