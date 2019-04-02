import xlrd
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ProjectVar.var import *

class parseExcel(object):
    def __init__(self,excelPath):
        self.excelPath=excelPath
        self.wkb=xlrd.open_workbook(self.excelPath)
        self.sheet=self.wkb.sheets()[0]  #默认打开第一个sheet

    def set_sheet_by_name(self,sheetname):
        #切换sheet
        self.sheet=self.wkb.sheet_by_name(sheetname)
        return self.sheet

    def get_sheet_by_name(self):
        #获取sheetname
        return self.wkb.sheet_by_name(sheetname)

    def get_row_count(self):
        #总行数
        return self.sheet.nrows

    def get_col_count(self):
        #总列数
        return self.sheet.ncols

    def get_row(self,rowNum):
        #获取某一行数据，第一行从0开始
        return self.sheet.row_values(rowNum)

    def get_cell(self,rowNum,colNum):
        #获取某一单元格数据，第一行从0开始
        return self.sheet.cell_value(rowNum,colNum)

    def get_dict(self,rowNum):
        #获取数据字典，带数据标题
        #适用于数据列特别多的情况
        dictRet={}
        if rowNum>=self.get_row_count():
            raise Exception('不存在第'+str(rowNum+1)+'行')

        titles=self.get_row(0)
        datas=self.get_row(rowNum)

        i=0
        while i<self.get_col_count():
            dictRet[titles[i]]=self.normalize_cell(rowNum,i)
            i=i+1

        print(dictRet)
        return dictRet

    def normalize_cell(self,row,col):
        #规范化数据类型
        value=self.get_cell(row,col)
        type=self.sheet.cell_type(row,col)
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
            value=value.strftime("%Y-%m-%d")
        elif type==4:
            #Bool型
            value=True if value==1 else False
        return value

if __name__=='__main__':
    parseExcel=parseExcel(test_data_path)
    print(parseExcel.get_row(1))
    print('数据--'+parseExcel.get_cell(1,3))
    print(parseExcel.get_dict(1))
