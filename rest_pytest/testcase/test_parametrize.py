import pytest

@pytest.mark.parametrize("test_input,excepted",[("3+5",8),("2+4",6),("6*9",42),])
def test_eval(test_input,excepted):
    assert eval(test_input)==excepted

if __name__=="__main__":
    pytest.main("-s  D:/Git/pyrequest/rest_pytest/testcase/test_parametrize.py")
