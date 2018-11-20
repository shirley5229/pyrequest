import json
import os,sys
import time,datetime

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# D:\Git\pyrequest\tms3_rest_test\interface
parentdir = parentdir.split('\interface')[0]
sys.path.insert(0,parentdir)
from db_fixture import test_data

def  getPrimStatus(dbConfig,primid):
    '''获取单据状态，用于断言 '''
    consdata = test_data.getPrimInfo(dbConfig,primid)
    oradata = consdata['data'][0]
    return oradata['primStatus']

def  getPrimExist(dbConfig,primid):
    '''获取单据是否存在，用于断言 '''
    consdata = test_data.getPrimInfo(dbConfig,primid)
    oradata = consdata['rowcount']
    return oradata

def  getFileID(dbConfig,primid,filename):
    '''获取附件是否存在，用于断言 '''
    consdata = test_data.getAttechment(dbConfig,primid,filename)
    return consdata
