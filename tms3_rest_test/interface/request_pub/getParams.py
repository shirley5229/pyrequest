import json
import os,sys
import time,datetime
from . import config
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# D:\Git\pyrequest\tms3_rest_test\interface
parentdir = parentdir.split('\interface')[0]
sys.path.insert(0,parentdir)
from public import log
from db_fixture import test_data

log = log.setLog()

def getParam_cancelConsultation(dbConfig,logicName,prim_no,errorid=''):
    '''取消会诊，构建参数'''
    if not logicName:
        raise("logicName不能为空!")

    params = {}
    params["LOGICNAME"]=logicName
    params["TOKEN"]='1'
    params["MESSAGEID"]='2'
    datas={}

    if prim_no:
        if not dbConfig:
            raise("dbConfig不能为空!")
        consdata=test_data.getPrimInfo(dbConfig,prim_no)
        oradata=consdata["data"][0]
        datas["id"] = oradata["primid"]
    else:
        datas["id"] = errorid

    datas["userId"]="userId"
    datas["remark"]="remark"

    params["DATAS"] = datas
    log.info('接口参数为' + str(json.dumps(params)))
    return params


def getParam_saveFile(dbConfig,logicName,prim_no,filename,nullParam=''):
    '''获取附件，构建参数'''
    params = {}
    params['LOGICNAME']=logicName
    params['TOKEN']=''
    params['MESSAGEID']=''
    datas={}

    #从申请端数据库获取数据
    consdata=test_data.getAttechment(dbConfig,prim_no,filename)
    oradata=consdata['data'][0]
    datas['filename']=oradata['filename']
    datas['srcsid']=oradata['srcsid']
    datas['attachmenttype']=oradata['attachmenttype']
    datas['url']= config.file_url+"md5="+oradata['md5']+"&bizId="+oradata['srcsid']

    if nullParam=='filename':
        datas['filename']=''
    elif  nullParam=='url':
        datas['url']=''
    elif  nullParam=='srcsid':
        datas['srcsid']=''
    elif  nullParam=='attachmenttype':
        datas['attachmenttype']=''

    params['DATAS'] = datas
    log.info('接口参数为' + str(json.dumps(params)))
    return params


def getParam_sendStatus(dbConfig,logicName,prim_no,nullParam='',errorid=''):
    '''更改单据状态，构建参数'''
    params = {}
    params['LOGICNAME']=logicName
    params['TOKEN']=''
    params['MESSAGEID']=''
    datas={}

    #从会诊端数据库获取数据
    consdata=test_data.getStepStatus(dbConfig,prim_no)
    oradata=consdata['data'][0]
    datas['id']=oradata['id']
    datas['status']=oradata['status']
    datas['statusName']=oradata['statusName']
    datas['consUserId']=oradata['consUserId']
    datas['remark']=oradata['remark']

    if nullParam=='id':
        datas['id']=''
    elif  nullParam=='status':
        datas['status']=''
    elif  nullParam=='statusName':
        datas['statusName']=''

    if errorid:
        datas['id'] = errorid
        
    params['DATAS'] = datas
    log.info('接口参数为' + str(json.dumps(params)))
    return params

def getParam_getReport(dbConfig,logicName,prim_no,errorid=''):
    '''获取报告，构建参数'''
    params = {}
    params['LOGICNAME']=logicName
    params['TOKEN']=''
    params['MESSAGEID']=''
    datas={}
    if prim_no:
        consdata=test_data.getPrimInfo(dbConfig,prim_no)
        oradata = consdata['data'][0]
        datas['id']=oradata['primid']
    else:
        datas['id']=errorid

    params['DATAS']=datas
    log.info('接口参数为' + str(json.dumps(params)))
    return params

def getParam_reject(dbConfig,logicName,prim_no,nullParam=''):
    '''退回单据，构建参数'''
    params = {}
    params['LOGICNAME']=logicName
    params['TOKEN']=''
    params['MESSAGEID']=''

    datas={}
    consdata=test_data.getStepReject(dbConfig,prim_no)
    oradata = consdata['data'][0]
    datas['id']=oradata['id']
    datas['opuserid']=oradata['opuserid']
    datas['opusername']=oradata['opusername']
    datas['remark']=oradata['remark']
    datas['rejectcause']=oradata['rejectcause']

    if nullParam=='id':
        datas['id']=''
    elif nullParam=='opuserid':
        datas['opuserid']=''
    elif nullParam=='opusername':
        datas['opusername']=''

    params['DATAS']=datas
    log.info('接口参数为' + str(json.dumps(params)))
    return params
