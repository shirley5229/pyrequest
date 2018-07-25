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
class SaveConsultationFileTest(unittest.TestCase):
    """会诊医生，接受会诊附件补传"""
    def setUp(self):
        self.dbConfig = "applyOracleConf"  #从申请端数据库获取数据
        self.logicName = "saveConsultationFile"
        self.log = log.setLog()


    @unittest.skip("test")
    def test_success(self):
        ''' 正常获取token'''
        self.log.info(self.logicName+':正确性测试')
        params=getParams.getParam_saveFile(self.dbConfig,self.logicName,config.primNo3,config.filename)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #在数据库中查找此附件
        self.assertEqual(getAssert.getFileExist(self.dbConfig,self.logicName,config.primNo3,config.filename),1,'附件没有同步成功!')

    @data('filename','url','srcsid')
    def test_null(self,nullParam):
        ''' 必填项传入空'''
        self.log.info(self.logicName+':'+nullParam+' 传入空')
        params=getParams.getParam_saveFile(self.dbConfig,self.logicName,config.primNo2,config.filename,nullParam)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"05")
        self.assertEqual(result['message'],"必填项为空",nullParam+"为空")

    @unittest.skip("test")
    def test_error1(self):
        ''' srcsid，在申请端存在，在会诊端不存在'''
        self.log.info(self.logicName+':srcsid错误性测试')
        params=getParams.getParam_saveFile(self.dbConfig,self.logicName,config.primNo03,config.filename,'')
        result=httpRequest.postRequest(config.cons_url,params)

        self.assertEqual(result['code'],"09")
        self.assertTrue("未查询到指定会诊信息" in result['message'])

if __name__=="__main__":
    unittest.main(verbosity=2)
