import json
import os,sys
from . import config
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# D:\Git\pyrequest\tms3_rest_test\interface
parentdir = parentdir.split("\interface")[0]
sys.path.insert(0,parentdir)
from public import log
from public import excelOperation
from db_fixture import test_data

log = log.setLog()

#组织参数
#primid   根据会诊ID在申请端数据库查询数据
#imageexam   是否传递影像
#pathology    是否传递病理
#attechment    是否传递附件
#nullID     必填项为空测试
#excelRow     异常测试，在Excel中读取数据
def getParam(dbConfig,logicName,primid="",imageexam=0,pathology=0,attechment=0,
excelRow=0,nullID=""):
    params={"LOGICNAME":logicName}
    params["TOKEN"]=""
    params["MESSAGEID"]=""

    data={}
    oradata={}

    #正常测试，从申请医生数据库中取数
    #异常测试，从Excel中取数
    if excelRow:
        oradata= excelOperation.getRowData("/data/consultationData.xlsx","data",1)
    else:
        consdata=test_data.getConsultation(dbConfig,primid)
        oradata = consdata["data"][0]

    data["primid"]=oradata["primid"]
    data["patientid"]=oradata["patientid"]
    data["patientno"]=oradata["patientno"]
    data["patientname"]=oradata["patientname"]
    data["patientage"]=str(oradata["patientage"])
    data["patientageunitid"]=oradata["patientageunitid"]
    data["patientgender"]=oradata["patientgender"]
    #datetime.datetime 转为string
    if oradata["patientbirthday"]:
        data["patientbirthday"]=oradata["patientbirthday"].strftime("%Y-%m-%d")
    data["patientphone"]=oradata["patientphone"]
    data["patientaddress"]=oradata["patientaddress"]
    data["idnumber"]=oradata["idnumber"]
    data["job"]=oradata["job"]
    data["patientfolk"] = oradata["patientfolk"]
    data['patientnation']=oradata['patientnation']
    data["patientheight"] = str(oradata["patientheight"])
    data["patientweight"] = str(oradata["patientweight"])

    if oradata["applytime"]:
        data["applytime"] = oradata["applytime"].strftime("%Y-%m-%d")
    #临床病例
    data["chiefcomplaint"] = oradata["chiefcomplaint"]
    data["clinmedicalhistory"]=oradata["clinmedicalhistory"]
    data["pasthistory"] =oradata["pasthistory"]
    data["allergyhistory"]=oradata["allergyhistory"]
    data["illnesshistory"] =oradata["illnesshistory"]
    data["familyhistory"]=oradata["familyhistory"]
    data["illness"] =oradata["illness"]
    data["examination"]=oradata["examination"]
    data["prediagnose"] =oradata["prediagnose"]
    data["takenmedicien"] = oradata["takenmedicien"]
    data["treatmentprocess"] = oradata["treatmentprocess"]
    data["chiefphysician"] = oradata["chiefphysician"]
    #end 临床病例
    data["reqconsult"] = oradata["reqconsult"]
    data["supplementinstruction"] = oradata["supplementinstruction"]
    data["patientstatusid"] = oradata["patientstatusid"]
    data["patienttypeid"] = oradata["patienttypeid"]
    data["maritalstatus"] = oradata["maritalstatus"]
    data["vip"] = oradata["vip"]
    data["consultationid"] = oradata["consultationid"]
    data["emergency"] = oradata["emergency"]
    data["applytype"] = oradata["applytype"]
    data["isschedule"] = oradata["isschedule"]
    data["requserid"] = config.requserid  #requserid在程序中写死
    data["reqhospitalid"]=oradata["reqhospitalid"]
    data["reqhospital"]= oradata["reqhospital"]
    data["reqdepartmentid"]= oradata["reqdepartmentid"]
    data["reqdepartment"]= oradata["reqdepartment"]
    data["reqdoc"]= oradata["reqdoc"]
    data["reqtelphone"]= oradata["reqtelphone"]
    data["diagtype"]= oradata["diagtype"]
    data["consmode"]= oradata["consmode"]
    data["consultationtypeid"]=oradata["consultationtypeid"]
    if oradata["inoroutdate"]:
        data["inoroutdate"] = oradata["inoroutdate"].strftime("%Y-%m-%d")
    data["healthcaretype"]=oradata["healthcaretype"]
    data["hctid"]=oradata["hctid"]

    #只测试primid为空
    if nullID=='primid':
        data["primid"]=''

    assignlist=[]
    assigninfo={}
    if logicName=='sendConsultation':
        assignRes=test_data.getTriage(dbConfig,primid)
        listData=assignRes["data"]
        for assigndata in listData:
            assigninfo["tria_hospid"] = assigndata["tria_hospid"]
            assigninfo["tria_deptid"] = assigndata["tria_deptid"]
            assigninfo["tria_subdeptid"] = assigndata["tria_subdeptid"]
            assigninfo["tria_docid"] = assigndata["tria_docid"]
            assigninfo["tria_main"] = assigndata["tria_main"]
            assigninfo["tria_depttype_id"] = assigndata["tria_depttype_id"]

            if nullID == 'assigndepartmentid':
                assigninfo["tria_subdeptid"] = ''
                assigninfo["tria_deptid"] = ''
            assignlist.append(assigninfo)
    if logicName=='saveConsultation':
        assignRes=test_data.getSaveTriage(dbConfig,primid)
        listData=assignRes["data"]
        for assigndata in listData:
            assigninfo["assignhospitalid"] = assigndata["assignhospitalid"]
            assigninfo["assigndepartmentid"] = assigndata["assigndepartmentid"]
            assigninfo["assignsubdeptid"] = assigndata["assignsubdeptid"]
            assigninfo["assigndocid"] = assigndata["assigndocid"]
            assigninfo["assigndepttypeid"] = assigndata["assigndepttypeid"]
            assigninfo["assigntriamain"] = assigndata["assigntriamain"]

            if nullID =='assigndepartmentid':
                assigninfo["assigndepartmentid"] = ''
                assigninfo["assignsubdeptid"] = ''
            assignlist.append(assigninfo)
    data["assigninfo"]=assignlist

    #传输影像数据
    if imageexam:
        imageexamRes=test_data.getImageexam(dbConfig,primid)
        listData=imageexamRes["data"]
        imageexamlist=[]
        for imagedata in listData:
            imageexam ={}
            imageexam["xeguid"]=imagedata["xeguid"]
            if imagedata["studytime"]:
                imageexam["studytime"]=imagedata["studytime"].strftime("%Y-%m-%d")
            imageexam["devicename"]=imagedata["devicename"]
            imageexam["devicetypename"]=imagedata["devicetypename"]
            imageexam["studydescribe"]=imagedata["studydescribe"]
            imageexam["studyid"]=imagedata["studyid"]
            imageexam["studyinstanceuid"]=imagedata["studyinstanceuid"]
            imageexam["url"]=imagedata["url"]
            imageexamlist.append(imageexam)
        data["imageexam"]=imageexamlist

    #传输病理数据
    if pathology:
        pathologyRes=test_data.getPathology(dbConfig,primid)
        listData=pathologyRes["data"]
        pathologylist=[]
        for pathologydata in listData:
            pathology={}
            pathology["sampleinfo"]=pathologydata["sampleinfo"]
            pathology["sampletype"]=pathologydata["sampletype"]
            pathology["samplecondition"]=pathologydata["samplecondition"]
            pathology["samplepart"]=pathologydata["samplepart"]
            pathology["partcount"]=pathologydata["partcount"]
            pathology["partunit"]=pathologydata["partunit"]
            pathology["applydoctor"]=pathologydata["applydoctor"]
            pathology["applyhospital"]=pathologydata["applyhospital"]
            if pathologydata["operatetime"]:
                pathology["operatetime"]=pathologydata["operatetime"].strftime("%Y-%m-%d")
            pathology["staining"]=pathologydata["staining"]
            pathology["immunohistochemical"]=pathologydata["immunohistochemical"]
            pathology["surgeryrecord"]=pathologydata["surgeryrecord"]
            pathology["allshow"]=pathologydata["allshow"]
            pathologylist.append(pathology)
        data["pathology"]=pathologylist

    #传输附件数据
    if attechment:
        attechmentRes=test_data.getAttechment(dbConfig,primid)
        listData=attechmentRes["data"]
        attechmentlist=[]
        for attechmentdata in listData:
            attechment={}
            attechment["filename"]=attechmentdata["filename"]
            attechment["Examtype"]=attechmentdata["Examtype"]
            attechment["Imagetype"]=attechmentdata["Imagetype"]
            attechment["checksystem"]=attechmentdata["checksystem"]
            attechment["describe"]=attechmentdata["describe"]

            if logicName=='sendConsultation':
                attechment["attechmenttype"]=attechmentdata["attechmenttype"]
                attechment["sourceurl"]= config.file_url+"md5="+attechmentdata['filemd5']+"&bizId="+attechmentdata['srcsid']
                attechment["filemd5"]=attechmentdata["filemd5"]
            elif logicName == 'saveConsultation':
                attechment["attachmenttype"]=attechmentdata["attechmenttype"]
                attechment["url"]= config.file_url+"md5="+attechmentdata['filemd5']+"&bizId="+attechmentdata['srcsid']
                attechment["md5"]=attechmentdata["filemd5"]
            else:
                raise('logicName传入错误')
            attechmentlist.append(attechment)
        data["attechmentlist"]=attechmentlist

    params["DATAS"]=data
    log.info("接口" + str(params))
    return params
