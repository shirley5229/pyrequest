import json
import os,sys
import time,datetime

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# D:\Git\pyrequest\tms3_rest_test\interface
parentdir = parentdir.split('\interface')[0]
sys.path.insert(0,parentdir)
from tools import log
from db_fixture import test_data
from data import config

log = log.setLog()

def getParam_cancelConsultation(dbConfig,logicName,prim_no,errorid='',mustParam=0):
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

    if not mustParam:
        datas["userId"]=config.requserid
        datas["remark"]="取消会诊备注"

    params["DATAS"] = datas
    log.info('接口参数为' + str(params))
    return params


def getParam_saveFile(dbConfig,logicName,primid,filename,nullParam=''):
    '''获取附件，构建参数'''
    params = {}
    params['LOGICNAME']=logicName
    params['TOKEN']=''
    params['MESSAGEID']=''
    datas={}

    #从申请端数据库获取数据
    consdata=test_data.getAttechment(dbConfig,primid,filename)
    oradata=consdata['data'][0]
    datas['filename']=oradata['filename']
    datas['srcsid']=oradata['srcsid']
    datas['url']= config.file_url+"md5="+oradata['filemd5']+"&bizId="+oradata['srcsid']

    if nullParam=='filename':
        datas['filename']=''
    elif  nullParam=='url':
        datas['url']=''
    elif  nullParam=='srcsid':
        datas['srcsid']=''

    params['DATAS'] = datas
    log.info('接口参数为' + str(params))
    return params


def getParam_sendStatus(dbConfig,logicName,prim_no,statusCode,nullParam='',errorid='',mustParam=0):
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
    datas['status']=statusCode
    datas['triageSyn']='2'  #默认不同步
    #全部字段都传值
    if not mustParam:
        datas['consUserId']=oradata['consUserId']
        datas['remark']=logicName+"状态变更"+time.strftime('%Y-%m-%d %H%M%S')

        statusName = '会诊申请'
        if statusCode=='10':
            pass
        elif statusCode=='20':
            statusName ='前质控'
        elif statusCode=='30':
            statusName ='分配完成'
        elif statusCode=='40':
            statusName ='报告完成'
        elif statusCode=='50':
            statusName ='后质控完成'
        datas['statusName']=statusName

    if nullParam=='id':
        datas['id']=''
    elif  nullParam=='status':
        datas['status']=''
    elif  nullParam=='triageSyn' and logicName == 'saveStatus':
        datas['triageSyn']=''

    if errorid:
        datas['id'] = errorid

    params['DATAS'] = datas
    log.info('接口参数为' + str(params))
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
    log.info('接口参数为' + str(params))
    return params

def getParam_reject(dbConfig,logicName,prim_no,nullParam='',errorid='',mustParam=0):
    '''退回单据，构建参数'''
    params = {}
    params['LOGICNAME']=logicName
    params['TOKEN']=''
    params['MESSAGEID']=''

    datas={}
    consdata=test_data.getPrimInfo(dbConfig,prim_no)
    oradata = consdata['data'][0]
    datas['id']=oradata['primid']
    datas['opuserid']=config.requserid
    datas['opusername']='接口测试-南芬医院'
    datas['rejectcause']="接口测试"

    if not mustParam:
        datas['remark']="退回"+time.strftime('%Y-%m-%d %H%M%S')

    if nullParam=='id':
        datas['id']=''
    elif nullParam=='opuserid':
        datas['opuserid']=''
    elif nullParam=='opusername':
        datas['opusername']=''
    elif nullParam=='rejectcause':
        datas['rejectcause']=''

    if errorid=='id':
        datas['id']='00000009999'

    params['DATAS']=datas
    log.info('接口参数为' + str(params))
    return params
