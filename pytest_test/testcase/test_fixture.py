#coding=utf-8
import json
import pytest

@pytest.fixture(scope="module",params=['mod1','mod2'])
def modarg(request):
    param= request.param
    print("Setup modarg %s" % param)
    yield param
    print(" Teardown modarg %s" % param)

@pytest.fixture(scope="function",params=[1,2])
def otherarg(request):
    param= request.param
    print("Setup otherarg %s" % param)
    yield param
    print(" Teardown otherarg %s" % param)

def test_0(otherarg):
    print(" Run test0 with otherarg %s" % otherarg)

def test_1(modarg):
    print(" Run test1 with modarg %s" % modarg)

def test_2(otherarg,modarg):
    print(" Run test2 with otherarg %s and modarg %s " % (otherarg,modarg))

if __name__=="__main__":
    pytest.main('-v -s D:\Git\pyrequest\pytest_test\\test_fixture.py --collect-only ')
