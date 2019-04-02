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
    """接受会诊附件补传,异常性测试"""
    @classmethod
    def setUpClass(self):
        self.logicName = "saveConsultationFile"
        self.log = log.setLog()


    @data('filename','url','srcsid')
    def test_null(self,nullParam):
        ''' 必填项传入空'''
        self.log.info(self.logicName+':'+nullParam+' 传入空')
        params=getParams.getParam_saveFile(config.appDBConf,self.logicName,config.primid02,config.filename,nullParam)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"05")
        self.assertEqual(result['message'],"必填项为空",nullParam+"为空")


    def test_error1(self):
        ''' srcsid，在会诊端不存在,在申请端取数据'''
        self.log.info(self.logicName+':srcsid错误性测试')
        params=getParams.getParam_saveFile(config.appDBConf,self.logicName,config.primid4,config.filename,'')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"19")
        self.assertTrue("根据id查询会诊失败" in result['message'])

if __name__=="__main__":
    unittest.main(verbosity=2)
