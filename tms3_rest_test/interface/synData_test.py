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


class DataSynTest(unittest.TestCase):
    """机构信息同步，获取会诊端数据"""
    @classmethod
    def setUpClass(self):
        self.logicName = "dataSyn"
        self.log = log.setLog()

    def test_success(self):
        ''' 正确性测试'''
        self.log.info(self.logicName+':正确性测试')
        params=self.getParam('上海交通大学医学院附属瑞金医院')
        result=httpRequest.postRequest(config.consdata_url,params)

        self.assertEqual(result['responseStatus'],'0','responseStatus返回错误')
        self.assertEqual(result['message'],"数据同步成功！",'message返回错误')
        data=result['data']
        self.assertTrue(data !={},'data返回为空')
        self.assertTrue(len(data["tmsHospitalList"])>=1,'tmsHospitalList返回错误')
        self.assertTrue(len(["tmsDepartmentList"])>=1,'tmsDepartmentList返回错误')
        self.assertTrue(len(["tmsSubDepartmentList"])>=1,'tmsSubDepartmentList返回错误')
        self.assertTrue(len(["userList"])>=1,'userList返回错误')

    def test_null1(self):
        ''' platform_id为空'''
        self.log.info(self.logicName+':平台id为空')
        params=self.getParam('','platform_id')
        result=httpRequest.postRequest(config.consdata_url,params)
        self.assertEqual(result['responseStatus'],'2')
        self.assertEqual(result['message'],"平台id为空！")

    def test_null2(self):
        ''' hospital_id为空'''
        self.log.info(self.logicName+':平台id为空')
        params=self.getParam('','hospital_id')
        result=httpRequest.postRequest(config.consdata_url,params)
        self.assertEqual(result['responseStatus'],'6')
        self.assertEqual(result['message'],"医院id为空！")

    def test_error2(self):
        ''' platform_id传入错误值'''
        self.log.info(self.logicName+':platform_id传入错误值')
        params=self.getParam('上海交通大学医学院附属瑞金医院','','platform_id')
        result=httpRequest.postRequest(config.consdata_url,params)
        self.assertEqual(result['responseStatus'],'4')
        self.assertEqual(result['message'] ,"没有查询到同步信息！")

    @unittest.skip("当token功能关闭，hospital_id没有作用")
    def test_error1(self):
        ''' hospital_id传入错误值'''
        self.log.info(self.logicName+':hospital_id传入错误值')
        params=self.getParam('','','hospital_id')
        result=httpRequest.postRequest(config.consdata_url,params)
        self.assertEqual(result['responseStatus'],'4')
        self.assertEqual(result['message'] ,"没有查询到同步信息！")


    def getParam(self,hospitalName,nullParam='',errorid=''):
        params = {}
        params['logicName']='dataSyn'
        params['token']=''
        params['messageId']=''
        datas={}
        if hospitalName:
            consdata=test_data.gethospitalID(config.consDBConf,hospitalName)
            oradata = consdata['data'][0]
            datas['hospital_id']=oradata['hospitalID']
        datas['platform_id']=config.platform_id

        if nullParam=='hospital_id':
            datas['hospital_id']=''
        elif nullParam=='platform_id':
            datas['platform_id']=""

        if errorid=='hospital_id':
            datas['hospital_id']='errorid'
        elif errorid=='platform_id':
            datas['platform_id']="1099002"

        params['datas']=datas
        self.log.info('接口参数为' + str(json.dumps(params)))
        return params

if __name__=="__main__":
    unittest.main(verbosity=2)
