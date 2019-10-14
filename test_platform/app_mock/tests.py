from django.test import TestCase
import requests
import json


# 测试：更新API操作
class ApiUpdateTest(TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/"

    def test_home(self):
        r = requests.get(self.base_url + "v2/home")
        result = r.json()
        # 更新价格为 99999
        result["result"]["groups"][1]["items"][0]["selling_price"] = 99999
        # 重新将数据保存
        result_json = json.dumps(result)
        r = requests.put(self.base_url + "v2/home", data={"response": result_json})
        ret = r.json()
        print(ret)


