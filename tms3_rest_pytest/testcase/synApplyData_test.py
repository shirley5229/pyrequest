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

class ApplyDataSynTest(unittest.TestCase):
    """机构信息，申请端同步数据"""
    def setUp(self):
        self.dbConfig = "applyOracleConf"
        self.logicName = "applyDataSyn"
        self.log = log.setLog()

    def test_success(self):
        ''' 正确性测试'''
        self.log.info(self.logicName+':正确性测试')
        params=self.getParam()
        result=httpRequest.postRequest(config.appdata_url,params)
        self.assertEqual(result['responseStatus'],'1')
        self.assertEqual(result['message'],"业务处理成功")

    def test_null(self):
        '''platform_id为空'''
        self.log.info(self.logicName+':必填项platform_id为空')
        params=self.getParam("null")
        result=httpRequest.postRequest(config.appdata_url,params)
        self.assertEqual(result['responseStatus'],'2')
        self.assertEqual(result['message'],"平台id为空！")


    @unittest.skip("无法测试")
    def test_fail(self):
        ''' platform_id传入错误值'''
        self.log.info(self.logicName+':platform_id传入错误值')
        params=self.getParam("111111122222")
        result=httpRequest.postRequest(config.appdata_url,params)
        self.assertEqual(result['code'],'2')
        self.assertEqual(result['message'],"platform_id不存在")


    def getParam(self,errorid=''):
        params = {}
        params['logicName']='applyDataSyn'
        params['token']=''
        params['messageId']=''
        datas={}
        if not errorid:
            datas['platform_id']=config.platform_id
        elif errorid=='null':
            datas['platform_id']=""
        else:
            datas['platform_id']=errorid

        params['datas']=datas
        self.log.info('接口参数为' + str(json.dumps(params)))
        return params

if __name__=="__main__":
    unittest.main(verbosity=2)
