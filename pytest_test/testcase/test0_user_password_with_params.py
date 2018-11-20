#coding=utf-8
import json
import pytest
users = json.loads(open('./users.dev.json','r').read())

class TestUserPassword(object):
    """docstring for TestUserPassword."""
    @pytest.fixture(params = users)
    def user(self,request):
        return request.param

    def test_user_password(self,user):
        #遍历每条user
        passwd=user['password']
        assert len(passwd) >= 6,'password cannot less than 6'
        msg = "user %s has a weak password" %(user['name'])
        assert passwd !="password",msg
        assert passwd !="password123",msg
