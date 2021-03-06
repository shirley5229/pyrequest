#coding=utf-8
import time,sys,os
import unittest
import HTMLTestRunner
sys.path.append('./interface')
sys.path.append('./db_fixture')

parentdir = os.path.dirname(os.path.abspath(__file__))
#D:\Git\pyrequest\tms3_rest_test
#parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
print(sys.path)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data
from interface.request_pub import httpRequest

#指定测试用例为当前文件夹下的interface目录
test_dir = parentdir + '/interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')


if __name__=="__main__":
    #删除会诊端数据
    #test_data.deleteConsData('onsOracleConf','20180611003')
    httpRequest.initData()
    '''
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    module_path = os.path.dirname(os.path.abspath(__file__))
    print(module_path)
    filename =module_path + '/report/'+now + '_result.html'
    fp = open(filename,'wb')
    runner = unittest.TextTestRunner(verbosity=2)
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'TMS3 Test Report',description=u'远程会诊3.0接口测试报告')
    runner.run(discover)

    fp.close()
    '''
