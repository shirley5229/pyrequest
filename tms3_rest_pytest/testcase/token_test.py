import json
import os,sys
import pytest
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data
from tools import log
from data import config
from testpub import httpRequest
from testpub import getParams

class TokenTest(object):
    """获取token测试"""
    def __init__(self):
        self.logicName = "createToken"
        self.log = log.setLog()

    def test_success(self):
        ''' 正常获取token'''
        self.log.info(self.logicName+':正确性测试')
        params=self.getParam('上海交通大学医学院附属瑞金医院')
        result=httpRequest.postRequest(config.token_url,params)
        assert result['responseStatus'] == '1'
        assert result['message'] == "创建并获取token成功！"
        assert result['data']['token_id'] != ''

    def test_null(self):
        ''' 医院ID为空'''
        self.log.info(self.logicName+':医院ID为空')
        params=self.getParam('','')
        result=httpRequest.postRequest(config.token_url,params)
        assert result['responseStatus'] == '2'
        assert result['message'] == "平台id为空！"

    def test_error(self):
        ''' 医院ID为错误值'''
        self.log.info(self.logicName+':医院ID为错误值')
        params=self.getParam('','12626266262')
        result=httpRequest.postRequest(config.token_url,params)
        assert result['responseStatus'] == '3'
        assert result['message'] =="平台id没有权限获取Token，请去平台信息配置中配置！"


    def getParam(self,hospitalName,errorid=''):
        params = {}
        params['logicName']='createToken'
        params['token']=''
        params['messageId']=''
        datas={}
        if hospitalName:
            consdata=test_data.gethospitalID(config.appDBConf,hospitalName)
            oradata = consdata['data'][0]
            datas['platform_id']=oradata['hospitalID']
        else:
            datas['platform_id']=errorid

        params['datas']=datas
        self.log.info('接口参数为' + str(params))
        return params

if __name__=="__main__":
    pytest.main('D:\\Git\pyrequest\\tms3_rest_pytest\\testcase\\token_test.py -s')
