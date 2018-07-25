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
    """申请医生，发起会诊申请"""
    def setUp(self):
        self.dbConfig = "applyOracleConf"
        self.logicName = "sendConsultation"
        self.log = log.setLog()

    #操作步骤，
    #在申请端创建单据
    #根据prim_no在数据库中查找单据信息，赋给参数params，进行验证
    @unittest.skip("test")
    def test_success1(self):
        ''' 全部字段'''
        self.log.info(self.logicName+':正确性测试')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo2),1,'单据未同步成功')


    def test_success2(self):
        ''' 必填字段'''
        self.log.info(self.logicName+':必填字段')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"200")
        message=json.loads(result['message'])
        self.assertEqual(message['message'],"请求成功")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo1),1,'单据未同步成功')

    @unittest.skip("test")
    def test_success3(self):
        '''重复发送会诊'''
        self.log.info(self.logicName+':重复发送会诊')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"200")
        self.assertEqual(result['message'],"{\"code\":null,\"message\":\"请勿重复发送会诊！\",\"datas\":null}")


    @unittest.skip("test")
    def test_Imageexam(self):
        '''影像'''
        self.log.info(self.logicName+':申请影像会诊测试')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"创建并获取token成功！")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo2),1,'单据未同步成功')

    @unittest.skip("病理未启用，暂时不测试")
    def test_pathology(self):
        '''病理'''
        self.log.info(self.logicName+':申请病理会诊测试')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,0,1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"创建并获取token成功！")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo2),1,'单据未同步成功')

    @unittest.skip("test")
    def test_attechment(self):
        '''附件'''
        self.log.info(self.logicName+':申请会诊带附件')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,0,0,1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"创建并获取token成功！")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo2),1,'单据未同步成功')

    #异常测试，使用Excel
    @unittest.skip("test")
    @data(1,2,3,4,5,6,7,8,9,10,11,12)
    def test_null1(self,rowNum):
        '''patientname传入空'''
        self.log.info(self.logicName+':传入空')
        #调用Excel中数据
        params = getConsParams.getParam(self.dbConfig,self.logicName,'',0,0,0,rowNum)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"05")
        self.assertEqual(result['message'],"必填项为空")

    def test_null1(self):
        '''primid传入空'''
        self.log.info(self.logicName+':primid传入空')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,0,0,0,0,'primid')
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"05")
        self.assertEqual(result['message'],"必填项为空")

    @unittest.skip("test")
    @data('patientbirthday','consstart','inoroutdate')
    def test_error(self,errorDate):
        '''日期传入错误值'''
        self.log.info(self.logicName+':日期传入错误值')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,0,0,0,0,0,errorDate)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"06")
        self.assertEqual(result['message'],"日期转换错误")

if __name__=="__main__":
    unittest.main(verbosity=2)
