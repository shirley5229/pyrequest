#coding=utf-8
import time,sys,os
import pytest
sys.path.append('./interface')
sys.path.append('./db_fixture')
parentdir = os.path.dirname(os.path.abspath(__file__))
#D:\Git\pyrequest\tms3_rest_test
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from public import httpRequest
from public import function

if __name__=="__main__":
    #删除会诊端数据
    #test_data.deleteConsData('onsOracleConf','20180611003')
    httpRequest.initData()

    reportName = function.get_filepath("/report/")+"report_"+time.strftime('%Y-%m-%d')+".html"
    pytest.main(function.get_filepath("/interface/")+" --html="+reportName)
