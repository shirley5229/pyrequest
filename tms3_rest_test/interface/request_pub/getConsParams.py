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
#prim_no   根据会诊序号在申请端数据库查询数据
#imageexam   在申请端数据库查询数据
#pathology    在申请端数据库查询数据
#attechment    在申请端数据库查询数据
#excelRow     异常测试，在Excel中读取数据
def getParam(dbConfig,logicName,prim_no="",imageexam=0,pathology=0,attechment=0,
excelRow=0,nullID="",errorID=""):
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
        consdata=test_data.getConsultation(dbConfig,prim_no)
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
    if oradata["consstart"]:
        data["consstart"] = oradata["consstart"].strftime("%Y-%m-%d")
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
    data["requserid"] = "74ddaddc922d45d5bd1e6f4560d96ab8"  #oradata["requserid"]
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

    if nullID=='primid':
        data["primid"]=''

    if errorID=="patientbirthday":
        data["patientbirthday"] = "2018/6/26"
    elif errorID=="consstart":
        data["consstart"] = "20180626"
    elif errorID=="inoroutdate":
        data["inoroutdate"] = "26/6/2018"
    elif errorID=="requserid":
        data["requserid"] = "1111111111"
    elif errorID=="reqhospitalid":
        data["reqhospitalid"] = "222222222"
    elif errorID=="reqdepartmentid":
        data["reqdepartmentid"] = "33333333333"

    assignlist=[]
    assigninfo={}
    if logicName=='sendConsultation':
        assignRes=test_data.getTriage(dbConfig,prim_no)
        listData=assignRes["data"]
        for assigndata in listData:
            assigninfo["tria_id"] = assigndata["tria_id"]
            assigninfo["prim_id"] = assigndata["prim_id"]
            assigninfo["tria_hospid"] = assigndata["tria_hospid"]
            assigninfo["tria_deptid"] = assigndata["tria_deptid"]
            assigninfo["tria_subdeptid"] = assigndata["tria_subdeptid"]
            assigninfo["tria_docid"] = assigndata["tria_docid"]
            assigninfo["tria_hospname"] = assigndata["tria_hospname"]
            assigninfo["tria_deptname"] = assigndata["tria_deptname"]
            assigninfo["tria_subdeptname"] = assigndata["tria_subdeptname"]
            assigninfo["tria_docname"] = assigndata["tria_docname"]
            assigninfo["hospital_province"] = assigndata["hospital_province"]
            assigninfo["tria_main"] = assigndata["tria_main"]
            assigninfo["tria_type"] = assigndata["tria_type"]
            assigninfo["prim_id"] = assigndata["prim_id"]
            if assigndata["start_time"]:
                assigninfo["start_time"] = assigndata["start_time"].strftime("%Y-%m-%d")
            assigninfo["end_time"] = assigndata["end_time"]
            assigninfo["room_id"] = assigndata["room_id"]
            assigninfo["flag"] = assigndata["flag"]
            if assigndata["create_time"]:
                assigninfo["create_time"] = assigndata["create_time"].strftime("%Y-%m-%d")
            if assigndata["update_time"]:
                assigninfo["update_time"] = assigndata["update_time"].strftime("%Y-%m-%d")
            assigninfo["create_operator"] = assigndata["create_operator"]
            assigninfo["update_operator"] = assigndata["update_operator"]
            assignlist.append(assigninfo)
    if logicName=='saveConsultation':
        assignRes=test_data.getSaveTriage(dbConfig,prim_no)
        listData=assignRes["data"]
        for assigndata in listData:
            assigninfo["assignhospitalid"] = assigndata["assignhospitalid"]
            assigninfo["assigndepartmentid"] = assigndata["assigndepartmentid"]
            assigninfo["assignsubdeptid"] = assigndata["assignsubdeptid"]
            assigninfo["assigndocid"] = assigndata["assigndocid"]
            assigninfo["assigndepttypeid"] = assigndata["assigndepttypeid"]
            assigninfo["assigntriamain"] = assigndata["assigntriamain"]
            assignlist.append(assigninfo)
    data["assigninfo"]=assignlist

    #影像
    if imageexam:
        imageexamRes=test_data.getImageexam(dbConfig,prim_no)
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

    #病理
    if pathology:
        pathologyRes=test_data.getPathology(dbConfig,prim_no)
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

    #附件
    if attechment:
        attechmentRes=test_data.getAttechment(dbConfig,prim_no)
        listData=attechmentRes["data"]
        attechmentlist=[]
        for attechmentdata in listData:
            attechment={}
            attechment["filename"]=attechmentdata["filename"]
            attechment["attachmenttype"]=attechmentdata["attachmenttype"]
            attechment["url"]= config.file_url+"md5="+attechmentdata['md5']+"&bizId="+attechmentdata['srcsid']
            attechment["md5"]=attechmentdata["md5"]
            attechment["Examtype"]=attechmentdata["Examtype"]
            attechment["Imagetype"]=attechmentdata["Imagetype"]
            attechment["checksystem"]=attechmentdata["checksystem"]
            attechment["describe"]=attechmentdata["describe"]
            attechmentlist.append(attechment)
        data["attechmentlist"]=attechmentlist

    params["DATAS"]=data
    log.info("接口" + str(params))
    return params
