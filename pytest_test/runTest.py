import time,sys,os
import pytest
sys.path.append('./interface')
sys.path.append('./db_fixture')
import HTMLTestRunner
parentdir = os.path.dirname(os.path.abspath(__file__))
print(parentdir)
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data

if __name__=="__main__":
    #test_data.init_data()
    pytest.main("D:\Git\pyrequest\pytest_test\\testcase --html=D:\Git\pyrequest\pytest_test\\report\\report.html")
