import requests
import pytest

class TestV2exApi(object):
    """docstring for TestV2exApi."""
    domain = "https://www.v2ex.com/"

    @pytest.fixture(params=['python','java','go','nodejs'])
    def lang(self,request):
        return request.param

    def test_node(self,lang):
        path = 'api/nodes/show.json?name=%s'%(lang)
        url = self.domain + path
        res = requests.get(self.domain + path).json()
        assert res["name"] == lang
        assert 0
