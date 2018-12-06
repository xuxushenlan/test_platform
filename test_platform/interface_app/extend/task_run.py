import unittest
from ddt import ddt, data, file_data, unpack
import requests
import xmlrunner
import sys
import json
from os.path import dirname, abspath
interface_app_path = dirname(dirname(dirname(abspath(__file__))))
print("if_path", interface_app_path)
sys.path.append(interface_app_path)
from interface_app.apps import TASK_PATH


# global case1
# global case2
#
# case = {'first': 1, 'second': 3, 'third': 2}
# case1 = {'url': 'http://httpbin.org/post', 'method': 'post', 'data': {'key': 'value'}}
# case2 = {'url': 'https://api.github.com/events', 'method': 'get', 'data': {}}
# @data(case1, case2)


@ddt
class TaskRun(unittest.TestCase):

    @unpack
    @file_data(TASK_PATH + "case_data.json")
    def test_run_tasks(self, url, method, type, header, parameter, assert_text):
        print("hhhhh", header)
        print("pppppp", parameter)
        if header == "{}":
            header_dict = {}
        else:
            header_dict = json.loads(header)

        if parameter == "{}":
            payload_dict = {}
        else:
            payload_dict = json.loads(parameter)

        if method == "get":
            if type == "from":
                r = requests.get(url, headers=header_dict, params=payload_dict)

        if method == "post":
            if type == "from":
                r = requests.post(url, data=payload_dict)
            elif type == "json":
                r = requests.post(url, json=payload_dict)


# 运行测试用例
def run_cases():
    with open(TASK_PATH + 'results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)


if __name__ == '__main__':
    run_cases()
