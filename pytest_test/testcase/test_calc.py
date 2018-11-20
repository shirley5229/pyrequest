import pytest
import time
import timeout_decorator

#=====fixture======
@pytest.fixture(scope='function')
def setup_function(request):
    print("setup_function called.")

def teardown_function():
    print("teardown_function called.")

@pytest.fixture(scope='module')
def setup_module(request):
    print("setup_module called.")

def teardown_module():
    print("teardown_module called.")

@timeout_decorator.timeout(3,use_signals=False)
def test_1(setup_function):
    print("Test_1 called.")
    time.sleep(5)

def test_2(setup_function):
    print("Test_2 called.")

def test_3(setup_function):
    print("Test_3 called.")

if __name__=='__main__':
    pytest.main('D:\Git\pyrequest\pytest_test\\testcase\\test_calc.py -s')
