import unittest
import json
import os,sys
from ddt import ddt,data

from request_pub import config
from request_pub import httpRequest
from request_pub import getAssert
from request_pub import getConsParams

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data
from public import log


@ddt
class SaveConsultationTest(unittest.TestCase):
    """接受会诊申请,异常性测试"""
    @classmethod
    def setUpClass(self):
        self.logicName = "saveConsultation"
        self.log = log.setLog()

    def test_null2(self):
        '''会诊科室id为空'''
        self.log.info(self.logicName+':会诊科室id为空')
        params = getConsParams.getParam(config.appDBConf,self.logicName,config.primid2,0,0,0,0,'assigndepartmentid')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['message'],"会诊科室id为空！")

if __name__=="__main__":
    unittest.main(verbosity=2)
