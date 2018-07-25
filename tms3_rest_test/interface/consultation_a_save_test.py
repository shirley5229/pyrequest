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
    """会诊医生，接受会诊申请"""
    def setUp(self):
        self.dbConfig='applyOracleConf'   #从申请端数据库获取数据
        self.logicName = "saveConsultation"
        self.log = log.setLog()

    #操作步骤，
    #在申请端创建单据
    #根据prim_no在数据库中查找单据信息，赋给参数params，进行验证
    def test_success1(self):
        ''' 正常获取token'''
        self.log.info(self.logicName+':正确性测试')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo02)
        result=httpRequest.postRequest(config.cons_url,params)
        #{'code': '00', 'message': '请求成功', 'datas': {'consultationid': '92be9c60d2684195bce9420e898041a2', 'id': 'a69aa461816146348890649bf597dedc'}}
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo02),1,'单据未同步成功')

    def test_success2(self):
        ''' 必填字段'''
        self.log.info(self.logicName+':必填字段')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo01)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo01),1,'单据未同步成功')

    @unittest.skip("pass")
    def test_success3(self):
        '''重复发送会诊'''
        self.log.info(self.logicName+':重复发送会诊')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo01)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['message'],"请勿重复发送会诊！")

    @unittest.skip("test")
    def test_Imageexam(self):
        '''影像'''
        self.log.info(self.logicName+':申请影像会诊测试')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,1)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo2),1,'单据未同步成功')

    @unittest.skip("test")
    def test_attechment(self):
        '''附件'''
        self.log.info(self.logicName+':申请会诊带附件')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,0,0,1)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #在数据库中查找此单据
        self.assertEqual(getAssert.getPrimExist(self.dbConfig,config.primNo2),1,'单据未同步成功')

    @unittest.skip("test")
    @data('patientbirthday','consstart','inoroutdate')
    def test_error(self,errorDate):
        '''日期传入错误值'''
        self.log.info(self.logicName+':日期传入错误值')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,0,0,0,0,'',errorDate)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"06")
        self.assertEqual(result['message'],"日期转换错误")

    @unittest.skip("test")
    @data('requserid','reqhospitalid','reqdepartmentid')
    def test_error1(self,errorID):
        '''基础数据ID传入错误值'''
        self.log.info(self.logicName+':基础数据ID传入错误值')
        params = getConsParams.getParam(self.dbConfig,self.logicName,config.primNo2,0,0,0,0,'',errorID)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"06")
        self.assertEqual(result['message'],"主数据信息异常","基础数据ID传入错误值")


if __name__=="__main__":
    unittest.main(verbosity=2)
