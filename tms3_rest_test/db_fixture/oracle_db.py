import cx_Oracle
import os
import configparser as cparser
import json

os.environ['NLS_LANG'] ='SIMPLIFIED CHINESE_CHINA.UTF8'
#========读取 db_config.ini 文件=======
def getdbConfig(oracleConf):
    '''存在多个数据库配置信息，根据oracleConf区分'''
    base_dir = str(os.path.dirname(os.path.dirname(__file__)))
    base_dir = base_dir.replace('\\','/')
    file_path = base_dir + "/db_config.ini"

    cf = cparser.ConfigParser()
    cf.read(file_path)

    #host = cf.get("applyOracleConf",'host')
    host = cf.get(oracleConf,'host')
    port = cf.get(oracleConf,"port")
    user = cf.get(oracleConf,"user")
    password = cf.get(oracleConf,"password")
    #'tms3/tms3@172.16.161.113:1521/orcl'
    info = user+'/'+password+'@'+host+':'+port+'/orcl'
    return info


#========Oracle基础操作=======
class DB:
    """Oracle基础操作."""
    def __init__(self,oracleConf):
        info=getdbConfig(oracleConf)
        self.connection =cx_Oracle.connect(info)

    def clear(self,table_name):
        '''清空表数据'''
        real_sql = "truncate table"+table_name+";"
        #real_sql = "delete from "+table_name+";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    def search(self,table_name,searchCon,whereCon="1=1"):
        '''查询数据'''
        real_sql = "SELECT "+searchCon +" FROM "+table_name + " WHERE "+whereCon
        print('查询语句为:' + real_sql)
        cursor= self.connection.cursor()
        cursor.execute(real_sql)

        fields=cursor.description  #获取字段
        row = cursor.fetchall()  #获取数据
        rowcount = cursor.rowcount  #获取查询行数
        if rowcount == 0:
            raise Exception('查询结果为空')

        list=[]
        for eachrow in row:
            print(eachrow)
            data={}
            for i in range(len(fields)):
                if eachrow[i]==None:
                    #当前字段内容为空，传入空字符串"",而不是None，方便JSON转化
                    data[fields[i][0]]=""
                else:
                    data[fields[i][0]]=eachrow[i]
            list.append(data)

        data={}
        data['rowcount'] = rowcount  #存储查询结果行数
        data['data']=list       #存储查询数据
        #{"data":[{"id":001,"name":"Max"},{"id":002,"name":"John"},……],"rowcount":2}
        print('查询结果为:' + str(data))
        cursor.close()
        return data

    def insert(self,table_name,table_data):
        '''插入数据'''
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        #示例：INSERT INTO Persons (LastName, Address) VALUES ('Wilson', 'Champs-Elysees')
        real_sql = "INSERT INTO "+table_name +"("+key+") VALUES("+value+")"
        #print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()
        cursor.close()
        self.close()

    def delete(self,table_name,whereCon):
        '''删除数据'''
        if not whereCon:
            raise("安全起见，请输入where条件!")
        real_sql = "DELETE FROM "+table_name +" WHERE "+whereCon
        print(real_sql)
        cursor= self.connection.cursor()
        #with self.connection.cursor() as cursor:
        cursor.execute(real_sql)
        self.connection.commit()
        cursor.close()

    def close(self):
        '''关闭连接'''
        self.connection.close()

if __name__=='__main__':
    db = DB("applyOracleConf")
    searchCon=('p.pati_id AS "patientid",p.pati_no AS "patientno",p.pati_name AS "patientname",P.PATI_AGE AS "patientage",'+\
    'P.PATI_AGE_UNIT AS "patientageunitid",P.PATI_GENDER AS "patientgender",P.PATI_BIRTHDAY AS "patientbirthday",P.PATI_TEL AS "patientphone",'+\
    'P.PATI_ADDRESS AS "patientaddress",P.PATI_IDENTITY AS "idnumber",P.PATI_PROFESSION AS "job",P.PATI_FOLK AS "patientfolk",'+\
    'P.PATI_NATION AS "patientnation",P.PATI_HEIGHT AS "patientheight",P.PATI_WEIGHT AS "patientweight",PR.CONS_START AS "consstart",'+\
    'P.CLIN_CHIEF_COMPLAINT AS "chiefcomplaint",P.CLIN_MEDICAL_HISTORY AS "clinmedicalhistory",P.CLIN_ALLERGY_HISTORY AS "pasthistory",P.CLIN_PHYS_EXAM AS "examination",'+\
    'P.CLIN_DIAGNOSE AS "prediagnose",P.CLIN_MEDICINE AS "takenmedicien",P.CLIN_TREATMENT AS "treatmentprocess",P.CLIN_PURPOSE AS "reqconsult",'+\
    'P.CLIN_COMMENT AS "supplementinstruction",P.PATI_ILLNESS_STATUS AS "patientstatusid",P.PATI_TYPE AS "patienttypeid",P.PATI_MARITAL_STATUS AS "maritalstatus",'+\
    'PR.CONSULTATION_ID AS "consultationid",PR.PRIM_EMERGENCY AS "emergency",P.PATI_APPLY_TYPE AS "applytype",PR.PRIM_RESERVATION AS "isschedule",'+\
    'PR.APPLY_DOCID AS "requserid",PR.APPLY_HOSPID AS "reqhospitalid",PR.SELF_HOSP AS "reqhospital",PR.APPLY_DEPTID AS "reqdepartmentid",'+\
    'PR.SELF_DEPT AS "reqdepartment",PR.SELF_DOC AS "reqdoc",PR.CONS_TYPE AS "diagtype",PR.PRIM_APPOINTED AS "consultationtypeid",'+\
    'P.PATI_HOSPITALIZED_TIME AS "inoroutdate",P.PATI_HEALTHCARE_TYPE AS "healthcaretype",P.PATI_HCTID AS "hctid"')
    table_name='tms_cons_patient p JOIN TMS_CONS_PRIMARY PR ON  P.PRIM_ID=PR.PRIM_ID '
    whereCon="PR.prim_no='20180413004' "
    db.search(table_name,searchCon,whereCon)
    db.close()
