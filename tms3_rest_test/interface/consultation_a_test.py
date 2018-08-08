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
class ConsultationProcessTest(unittest.TestCase):
    """正确性测试，会诊申请、附件补传、会诊取消"""
    def setUp(self):
        self.log = log.setLog()

    #操作步骤，
    #在申请端创建单据
    #根据prim_no在数据库中查找单据信息，赋给参数params，进行验证
    def test_a_saveCons1(self):
        '''saveConsultation,正确性测试'''
        self.log.info('saveConsultation:正确性测试')
        params = getConsParams.getParam(config.appDBConf,"saveConsultation",config.primid02)    #
        result = httpRequest.postRequest(config.cons_url,params)
        #{'code': '00', 'message': '请求成功', 'datas': {'consultationid': '92be9c60d2684195bce9420e898041a2', 'id': 'a69aa461816146348890649bf597dedc'}}
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'] ,"请求成功")
        self.assertEqual(result['datas']['id'],config.primid02,'单据未同步成功')


    def test_a_saveCons2(self):
        '''saveConsultation,必填字段'''
        self.log.info('saveConsultation:必填字段')
        params = getConsParams.getParam(config.appDBConf,"saveConsultation",config.primid01)
        result = httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        self.assertEqual(result['datas']['id'],config.primid01,'单据未同步成功')

    def test_a_saveCons3(self):
        '''saveConsultation,带附件'''
        self.log.info('saveConsultation: 申请会诊带附件')
        params = getConsParams.getParam(config.appDBConf,"saveConsultation",config.primid03,0,0,1)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        self.assertEqual(result['datas']['id'],config.primid03,'单据未同步成功')

    def test_a_sendCons1(self):
        '''sendConsultation,正确性测试'''
        self.log.info('sendConsultation:正确性测试')
        params = getConsParams.getParam(config.appDBConf,'sendConsultation',config.primid2)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"200")
        message=json.loads(result['message'])
        self.assertEqual(message['code'],"00")
        self.assertEqual(message['message'],"请求成功")
        self.assertEqual(message['datas']['id'],config.primid2,'单据未同步成功')

    def test_a_sendCons2(self):
        '''sendConsultation,必填字段'''
        self.log.info('sendConsultation:必填字段')
        params = getConsParams.getParam(config.appDBConf,'sendConsultation',config.primid1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"200")
        message=json.loads(result['message'])
        self.assertEqual(message['code'],"00")
        self.assertEqual(message['message'],"请求成功")
        self.assertEqual(message['datas']['id'],config.primid1,'单据未同步成功')

    def test_a_sendCons3(self):
        '''sendConsultation,申请会诊带附件'''
        self.log.info('sendConsultation:申请会诊带附件')
        params = getConsParams.getParam(config.appDBConf,'sendConsultation',config.primid3,0,0,1)
        result=httpRequest.postRequest(config.app_url,params)
        self.assertEqual(result['code'],"200")
        message=json.loads(result['message'])
        self.assertEqual(message['code'],"00")
        self.assertEqual(message['message'],"请求成功")
        self.assertEqual(message['datas']['id'],config.primid3,'单据未同步成功')

    def test_fileSave(self):
        ''' saveConsultationFile,正确性测试'''
        self.log.info('saveConsultationFile:正确性测试')
        params=getParams.getParam_saveFile(config.appDBConf,'saveConsultationFile',config.primid02,config.filename)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #{'message': '请求成功', 'datas': {'id': '876bf70efc634183887fe76c609df470'}, 'code': '00'}
        consdata = getAssert.getFileID(config.consDBConf,config.primid02,config.filename)
        self.assertTrue(consdata['rowcount']>=1,'附件未同步成功')
        oradata = consdata['data'][0]
        self.assertEqual(result['datas']['id'],oradata['id'],'单据未同步成功')

    def test_z_cancelSave1(self):
        ''' cancelConsultation,正确性测试'''
        self.log.info('cancelConsultation:正确性测试')
        params=getParams.getParam_cancelConsultation(config.appDBConf,'cancelConsultation',config.primid02)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #单据状态变为取消会诊=90
        self.assertEqual(getAssert.getPrimStatus(config.consDBConf,config.primid02),'90','单据状态未变为取消')

    def test_z_cancelSave2(self):
        '''cancelConsultation,必填项'''
        self.log.info('cancelConsultation:必填项')
        params=getParams.getParam_cancelConsultation(config.appDBConf,'cancelConsultation',config.primid03,'',1)
        result=httpRequest.postRequest(config.cons_url,params)
        self.assertEqual(result['code'],"00")
        self.assertEqual(result['message'],"请求成功")
        #单据状态变为取消会诊=90
        self.assertEqual(getAssert.getPrimStatus(config.consDBConf,config.primid03),'90','单据状态未变为取消')

if __name__=="__main__":
    unittest.main(verbosity=2)
