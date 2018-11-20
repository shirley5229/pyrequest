#coding=utf-8
import json
import pytest

class TestUserPassword(object):
    """docstring for TestUserPassword."""
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.dev.json','r').read())

    def test_user_password(self,users):
        #遍历每条user
        for user in users:
            passwd=user['password']
            assert len(passwd) >= 6,'password cannot less than 6'
            msg = "user %s has a weak password" %(user['name'])
            assert passwd !="password",msg
            assert passwd !="password123",msg
