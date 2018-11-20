import pytest
import time
import timeout_decorator

@pytest.mark.skip(reason="just test")
def test_reverse():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1/0
    assert excinfo.type=="RuntimeError"

@timeout_decorator.timeout(3,use_signals=False)
def test_timeout():
    time.sleep(5)

if __name__=='__main__':
    pytest.main('D:\\Git\\pyrequest\\pytest_test\\testcase\\test_exception.py -s')
