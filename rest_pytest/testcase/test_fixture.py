import pytest

@pytest.fixture(scope="module",params=['mod1','mod2'])
def modarg(request):
    param=request.param
    print("setup modarg %s"%param)
    yield param
    print("teardown modarg %s " % param)

@pytest.fixture(scope="function",params=[1,2])
def otherarg(request):
    param=request.param
    print("setup otherarg %s"%param)
    yield param
    print("teardown otherarg %s " % param)

def test_0(modarg):
    print("Run test0 with modarg %s" % modarg)

def test_1(otherarg):
    print("Run test1 with otherarg %s" % otherarg)

def test_2(modarg,otherarg):
    print("Run test2 with modarg %s and otherarg %s " % (modarg,otherarg))

if __name__=="__main__":
    pytest.main("-s D:/Git/pyrequest/rest_pytest/testcase/test_fixture.py")
