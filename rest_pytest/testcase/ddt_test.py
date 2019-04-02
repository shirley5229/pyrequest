import requests
import pytest
from ddt import ddt,data,unpack
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


@ddt
class Test_get():
	def setUp(self):
		pass

	@data(200,400,500)
	def test_get1(self,result):
		#get方法，不带参数
		r=requests.get('http://httpbin.org/get')
		assert r.status_code==result


	#@data(('id','0002'),('name','zhangsan'))
	@data(['id','0002'],['name','zhangsan'])
	@unpack
	def test_get2(self,key,value):
		#get方法，带参数params  headers
		params={key:value}
		print(params)
		r=requests.get('http://httpbin.org/get',params=params)
		print(r.json())    #返回响应信息
		resp=r.json()
		assert value==resp['args'][key]

if __name__=='__main__':
    #unittest.main(verbosity=2)
	pytest.main('D:/Git/pyrequest/rest_pytest/testcase/ddt_test.py')
