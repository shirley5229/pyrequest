import time,sys,os
import unittest
sys.path.append('./interface')
sys.path.append('./db_fixture')
import HTMLTestRunner
parentdir = os.path.dirname(os.path.abspath(__file__))
print(parentdir)
sys.path.insert(0,parentdir)
#需要跳转到pyrequest目录下引用db_fixture
from db_fixture import test_data

#指定测试用例为当前文件夹下的interface目录
test_dir = parentdir + '/interface'
print(test_dir)
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
print(discover)

if __name__=="__main__":
    #test_data.init_data()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    module_path = os.path.dirname(os.path.abspath(__file__))
    print(module_path)
    filename =module_path + '/report/'+now + '_result.html'
    fp = open(filename,'wb')
    #runner = unittest.TextTestRunner(verbosity=2)
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'Interface Test Report',description=u'Implem')
    runner.run(discover)
    fp.close()
