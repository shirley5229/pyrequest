import xlrd
import os
from public import function
from public import log

log=log.setLog()

def getRowData(path,sheetname,rowNum):
    #获取存储路径，脚本在test_case中，图片存储在与test_case平级的data中

    file_path=function.get_filepath(path)

    wkb=xlrd.open_workbook(file_path)
    sheet=wkb.sheet_by_name(sheetname)
    colNum=sheet.ncols     #总行数

    dictRet={}

    #若rowNum超出Excel边界，返回空字典
    if rowNum>=sheet.nrows:
        raise Exception('Excel中sheet页\''+sheetname+'\'不存在第'+str(rowNum+1)+'行')

    rowTitle=sheet.row_values(0)    #录入选项，列表类型
    rowValue=sheet.row_values(rowNum)   #第 行的数据

    #Excel把所有的数字都按 float 处理
    i=0
    while i<colNum:
        dictRet[rowTitle[i]]=readValue(sheet,rowNum,i)
        i=i+1

    log.info('Excel数据为:'+str(dictRet))
    return dictRet

def readValue(sheet,row,col):
    value=sheet.cell_value(row,col)
    type=sheet.cell_type(row,col)

    if type==1:
        #字符串
        pass
    elif type==2 and value % 1==0:
        #数字
        #value % 1==0 代表数据为整型，否则为浮点型
        value=int(value)
    elif type==3:
        #日期
        value=xlrd.xldate.xldate_as_datetime(value,0)
        #value=value.strftime("%Y-%m-%d")
    elif type==4:
        #Bool型
        value=True if value==1 else False
    return value


if __name__=='__main__':
     getRowData('/data/billdata.xlsx','hospital',1)

	#Screenshot_img(driver,time.strftime('%Y-%m-%d %H%M%S')+'baidu.jpg')
