import requests
import json
import os,sys
from . import config
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# D:\Git\pyrequest\tms3_rest_test\interface
parentdir = parentdir.split('\interface')[0]
sys.path.insert(0,parentdir)
from public import log
from db_fixture import test_data

log = log.setLog()

def postRequest(url,params):
    '''进行POST请求'''
    if not url or not params:
        raise("url和params不能为空!")

    headers = {'Content-type': 'application/json'}
    r = requests.post(url,data=json.dumps(params),headers=headers,timeout=5)
    #self.assertEqual(r.status_code,200,'接口返回异常')
    if r.status_code != 200:
        raise("接口返回异常")

    result=r.json()
    log.info('返回结果为:'+str(result))
    return result

#执行测试前，根据primid删除会诊端数据
def initData():
    primList=[config.primid1,config.primid2,config.primid3,
    config.primid01,config.primid02,config.primid03]
    for primid in primList:
        test_data.deleteConsData(config.consDBConf,primid)

if __name__=="__main__":
    initData()
