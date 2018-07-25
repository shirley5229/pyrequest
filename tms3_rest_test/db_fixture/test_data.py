import sys
sys.path.append('../db_fixture')
from .oracle_db import DB

#根据会诊序号，获取会诊ID、会诊状态
def getPrimInfo(oracleConf,prim_no):
    db=DB(oracleConf)
    searchCon=('PR.PRIM_ID AS "primid",PR.PRIM_STATUS AS "primStatus"')
    table_name=' TMS_CONS_PRIMARY PR '
    whereCon="PR.prim_no= '"+prim_no+"'"

    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#根据会诊序号，获取医院信息
def gethospitalID(oracleConf,hospitalName):
    db=DB(oracleConf)
    searchCon=(' H.HOSPITAL_ID AS "hospitalID" ')
    table_name=' TMS_HOSPITAL H '
    whereCon=" H.HOSPITAL_NAME='"+hospitalName+"'"

    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#获取会诊基础数据
def getConsultation(oracleConf,prim_no):
    db=DB(oracleConf)
    searchCon=('PR.PRIM_ID AS "primid",p.pati_id AS "patientid",p.pati_no AS "patientno",p.pati_name AS "patientname",P.PATI_AGE AS "patientage",'+\
       'P.PATI_AGE_UNIT AS "patientageunitid",P.PATI_GENDER AS "patientgender",P.PATI_BIRTHDAY AS "patientbirthday",P.PATI_TEL AS "patientphone",'+\
       'P.PATI_ADDRESS AS "patientaddress",P.PATI_IDENTITY AS "idnumber",P.PATI_PROFESSION AS "job",P.PATI_FOLK AS "patientfolk",PR.PRIM_IMPORTANT AS "vip",'+\
       'P.PATI_NATION AS "patientnation",P.PATI_HEIGHT AS "patientheight",P.PATI_WEIGHT AS "patientweight",PR.APPLY_TIME AS "consstart",'+\
       'P.CLIN_CHIEF_COMPLAINT   AS "chiefcomplaint",'+\
       'P.CLIN_MEDICAL_HISTORY   AS "clinmedicalhistory",'+\
       'P.CLIN_PAST_HISTORY   AS "pasthistory",'+\
       'P.CLIN_ALLERGY_HISTORY         AS "allergyhistory",'+\
       'P.CLIN_ILLNESS_HISTORY          AS "illnesshistory",'+\
       'P.CLIN_FAMILY_HISTORY          AS "familyhistory",'+\
       'P.CLIN_PHYS_EXAM         AS "illness",'+\
       'P.CLIN_ASSI_EXAM           AS "examination",'+\
       'P.CLIN_DIAGNOSE           AS "prediagnose",'+\
       'P.CLIN_MEDICINE    AS "takenmedicien",'+\
       'P.CLIN_TREATMENT         AS "treatmentprocess",'+\
       'P.CLIN_CHIEF_PHYSICIAN           AS "chiefphysician",'+\
       'P.CLIN_PURPOSE           AS "reqconsult",'+\
       'P.CLIN_COMMENT    AS "supplementinstruction",  '+\
       'P.PATI_ILLNESS_STATUS AS "patientstatusid",P.PATI_TYPE AS "patienttypeid",P.PATI_MARITAL_STATUS AS "maritalstatus",'+\
       'PR.CONS_MODE AS "consmode",PR.CONSULTATION_ID AS "consultationid",PR.PRIM_EMERGENCY AS "emergency",P.PATI_APPLY_TYPE AS "applytype",'+\
       'PR.PRIM_RESERVATION AS "isschedule", PR.APPLY_DOCID AS "requserid",PR.APPLY_HOSPID AS "reqhospitalid",PR.SELF_HOSP AS "reqhospital",'+\
       'PR.APPLY_DEPTID AS "reqdepartmentid",PR.SELF_DEPT AS "reqdepartment",PR.SELF_DOC AS "reqdoc",PR.SELF_DOCTEL AS "reqtelphone",PR.CONS_TYPE AS "diagtype",'+\
       'PR.PRIM_APPOINTED AS "consultationtypeid",P.PATI_HOSPITALIZED_TIME AS "inoroutdate",P.PATI_HEALTHCARE_TYPE AS "healthcaretype",P.PATI_HCTID AS "hctid"')
    table_name='tms_cons_patient p JOIN TMS_CONS_PRIMARY PR ON  P.PRIM_ID=PR.PRIM_ID '
    whereCon="PR.prim_no= '"+prim_no+"'"

    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#获取影像数据
def getImageexam(oracleConf,prim_no):
    db=DB(oracleConf)
    searchCon=('I.XEGUID AS "xeguid",I.STUDYTIME AS "studytime",I.DEVICENAME AS "devicename",I.DEVICETYPENAME AS "devicetypename",'+\
       'I.STUDYDESCRIBE AS "studydescribe",I.STUDYID AS "studyid",I.STUDYINSTANCEUID AS "studyinstanceuid",I.URL AS "url"')
    table_name='TMS_CONS_IMAGEEXAMINFO I JOIN TMS_CONS_PRIMARY PR ON I.PRIM_ID=PR.PRIM_ID'
    whereCon="PR.prim_no= '"+prim_no+"'"

    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#获取病理数据
def getPathology(oracleConf,prim_no):
    db=DB(oracleConf)
    searchCon=('PA.SEND_TYPE AS "sampleinfo",PA.SAMPLE_TYPE AS "sampletype",PA.SAMPLE_CONDITION AS "samplecondition",PA.SAMPLE_PART AS "samplepart",'+\
       'PA.SAMPLE_NUM AS "partcount",PA.PART_UNIT AS "partunit",PA.SEND_DOCTOR AS "applydoctor",PA.SEND_HOSPITAL AS "applyhospital",'+\
       'PA.SAMPLE_TIME AS "operatetime",PA.DYE AS "staining",PA.IMMUNO AS "immunohistochemical",PA.SURGERY_RECORD AS "surgeryrecord",'+\
       'PA.GENERAL_SHOW AS "allshow"')
    table_name='Tms_Cons_Pathology PA JOIN TMS_CONS_PRIMARY PR ON PA.PRIM_ID=PR.PRIM_ID'
    whereCon="PR.prim_no= '"+prim_no+"'"

    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#获取附件数据
def getAttechment(oracleConf,prim_no,filename=''):
    db=DB(oracleConf)
    searchCon=('A.FILENAME AS "filename",A.FILETYPE AS "attachmenttype",A.FILEMD5 AS "md5",'+\
       'A.EXAMTYPE AS "Examtype",A.IMAGETYPE AS "Imagetype",A.CHECKSYSTEM AS "checksystem",A.DESCRIBE AS "describe",PR.PRIM_ID AS "srcsid"')
    table_name='tms_attachment A LEFT JOIN TMS_CONS_PRIMARY PR ON A.BIZID=PR.PRIM_ID '
    whereCon="PR.prim_no= '"+prim_no+"' "
    if filename:
        whereCon +=" AND A.FILENAME='"+filename+"'"
    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#获取会诊退回数据
def getStepReject(oracleConf,prim_no):
    db=DB(oracleConf)
    searchCon=('* FROM (SELECT PR.PRIM_ID AS "id",R.OPERATORID AS "opuserid",U.USER_NAME AS "opusername",'+\
       'R.REJECT_REASON AS "rejectcause",R.REMARK AS "remark"')
    table_name=('TMS_CONS_PRIMARY PR RIGHT JOIN tms_step_record R ON R.PRIM_ID = PR.PRIM_ID'+\
        ' JOIN TMS_USER U ON R.OPERATORID=U.USER_ID')
    whereCon="R.REJECT_FLAG=1 AND PR.prim_no= '"+prim_no+"' ORDER BY R.CREATE_TIME desc) WHERE ROWNUM <= 1"
    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#获取会诊状态
def getStepStatus(oracleConf,prim_no):
    db=DB(oracleConf)
    searchCon=('* FROM (SELECT PR.PRIM_ID AS "id",PR.PRIM_STATUS AS "status",R.OPERATORID AS "consUserId",R.REMARK AS "remark",'+\
       'CASE PR.PRIM_STATUS WHEN \'10\' THEN \'会诊申请\' WHEN \'20\' THEN \'前质控\'  WHEN \'25\' THEN \'科室分诊\' WHEN \'30\' THEN \'分配完成\' '
       'WHEN \'40\' THEN \'报告完成\' WHEN \'50\' THEN \'后质控完成\' END AS "statusName"')
    table_name=('TMS_CONS_PRIMARY PR RIGHT JOIN tms_step_record R ON R.PRIM_ID = PR.PRIM_ID')
    whereCon="R.REJECT_FLAG=0 AND PR.prim_no= '"+prim_no+"' ORDER BY R.CREATE_TIME desc) WHERE ROWNUM <= 1"
    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#sendConsultation中assigninfo节点
def getTriage(oracleConf,prim_no):
    db=DB(oracleConf)
    searchCon=('T.TRIA_ID AS "tria_id",'+\
    'T.PRIM_ID AS "prim_id",'+\
    'T.TRIA_HOSPID AS "tria_hospid",'+\
    'T.TRIA_DEPTID AS "tria_deptid",'+\
    'T.TRIA_SUBDEPTID AS "tria_subdeptid",'+\
    'T.TRIA_DOCID AS "tria_docid", '+\
    'H.HOSPITAL_NAME AS "tria_hospname",'+\
    'D.DEPARTMENT_NAME AS "tria_deptname",'+\
    'SD.SUBDEPT_NAME AS "tria_subdeptname",'+\
    'U.USER_NAME AS "tria_docname",  '+\
    'H.HOSPITAL_PROVINCE AS "hospital_province",'+\
    'T.TRIA_DEPTTYPE_ID AS "tria_depttype_id",'+\
    'T.TRIA_MAIN AS "tria_main",'+\
    'T.TRIA_TYPE AS "tria_type",'+\
    'T.START_TIME AS "start_time",  '+\
    'T.END_TIME AS "end_time",'+\
    'T.ROOM_ID AS "room_id",'+\
    'T.FLAG AS "flag",'+\
    'T.CREATE_TIME AS "create_time",'+\
    'T.UPDATE_TIME AS "update_time",'+\
    'T.CREATE_OPERATOR AS "create_operator",'+\
    'T.UPDATE_OPERATOR AS  "update_operator"  ')
    table_name=(' TMS_CONS_TRIAGE T  '+\
    ' JOIN TMS_CONS_PRIMARY PR ON T.PRIM_ID = PR.PRIM_ID'+\
    ' JOIN TMS_HOSPITAL H ON T.TRIA_HOSPID = H.HOSPITAL_ID'+\
    ' JOIN TMS_DEPARTMENT D ON T.TRIA_DEPTID = D.DEPARTMENT_ID AND D.DEPT_HOSPITAL_ID=H.HOSPITAL_ID'+\
    ' JOIN TMS_SUBDEPARTMENT SD ON T.TRIA_SUBDEPTID=SD.SUBDEPT_ID AND SD.SUBDEPT_DEPT_ID= D.DEPARTMENT_ID'+\
    ' LEFT JOIN TMS_USER U ON T.TRIA_DOCID = U.USER_ID ')
    whereCon="PR.prim_no= '"+prim_no+"' "
    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#saveConsultation中assigninfo节点
def getSaveTriage(oracleConf,prim_no):
    db=DB(oracleConf)
    searchCon=('T.TRIA_HOSPID  AS "assignhospitalid",'+\
       'T.TRIA_DEPTID   AS "assigndepartmentid",'+\
       'T.TRIA_SUBDEPTID  AS "assignsubdeptid",'+\
       'T.TRIA_DOCID    AS "assigndocid",'+\
       'T.TRIA_DEPTTYPE_ID  AS "assigndepttypeid",'+\
       'T.TRIA_MAIN    AS "assigntriamain"')
    table_name=(' TMS_CONS_TRIAGE T  '+\
    ' JOIN TMS_CONS_PRIMARY PR ON T.PRIM_ID = PR.PRIM_ID')
    whereCon="PR.prim_no= '"+prim_no+"' "
    data=db.search(table_name,searchCon,whereCon)
    db.close()
    return data

#执行测试前，删除会诊端数据
def deleteConsData(oracleConf,primid):
    db=DB(oracleConf)

    #删除业务数据
    whereCon = " PRIM_ID ='"+primid+"'"
    whereCon2 = " BIZID ='"+primid+"'"
    tables=['tms_cons_comments','tms_cons_imageexaminfo','tms_cons_pathologyexaminfo','tms_cons_patient',
    'tms_cons_triage','tms_step_record','tms_cons_report','tms_cons_primary']
    for table_name in tables:
        db.delete(table_name,whereCon)
    db.delete('tms_attachment',whereCon2)
    #删除工作流
    searchCon=" OID"
    table_name="WF_BUSS_ORDER"
    whereCon="bid = '"+primid+"'"
    consdata=db.search(table_name,searchCon,whereCon)
    oradata=consdata['data'][0]
    oid=oradata['OID']  #获取工作流ID

    whereCon="order_id ='"+oid+"'"
    table_name="wf_task"
    db.delete(table_name,whereCon)
    whereCon="order_id ='"+oid+"'"
    table_name="wf_hist_task"
    db.delete(table_name,whereCon)
    whereCon="id ='"+oid+"'"
    table_name="WF_ORDER"
    db.delete(table_name,whereCon)
    whereCon="oid ='"+oid+"'"
    table_name="WF_BUSS_ORDER"
    db.delete(table_name,whereCon)

if __name__=='__main__':
    deleteConsData('consOracleConf','5ed66b5416e84079aca68fd3e499d28f')
