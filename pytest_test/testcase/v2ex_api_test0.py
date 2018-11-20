import requests
import pytest

class TestV2exApi(object):
    """docstring for TestV2exApi."""
    domain = "https://www.v2ex.com/"

    @pytest.mark.parametrize('name,node_id',[('python',90),('java',63),('go',375),('nodejs',436)])

    def test_node(self,name,node_id):
        path = 'api/nodes/show.json?name=%s'%(name)
        url = self.domain + path
        res = requests.get(self.domain + path).json()
        assert res["name"] == name
        assert res["id"] == node_id
