import os
import json
import threading
from time import sleep
from interface_app.models import TestTask, TestCase
from interface_app.apps import TASK_RUN_FILE, TASK_PATH
from xml.dom import minidom


class TaskThread:
    """
    通过多线程运行测试用例
    :param task_id: 任务ID
    :return:
    """

    def __init__(self, task_id):
        self.tid = task_id

    def run_cases(self, tid):
        task_obj = TestTask.objects.get(id=tid)
        cases_list = task_obj.cases.split(",")
        task_obj.status = 1  # 更新状态为运行中
        task_obj.save()

        cases_dict = {}
        for case_id in cases_list:
            if case_id == "":
                continue
            else:
                case_obj = TestCase.objects.get(id=int(case_id))
                case_dict = {
                    "url": case_obj.url,
                    "method": case_obj.req_method,
                    "type": case_obj.req_type,
                    "header": case_obj.req_header,
                    "parameter": case_obj.req_parameter,
                    "assert_text": case_obj.resp_assert,
                }
                cases_dict[case_obj.id] = case_dict

            cases_str = json.dumps(cases_dict)
            cases_data_file = TASK_PATH + "/case_data.json"
            with(open(cases_data_file, 'w')) as f:
                f.write(cases_str)

            os.system("python " + TASK_RUN_FILE)

    def save_result(self):
        """保存测试结果"""
        print("保存测试结果")
        dom = minidom.parse(TASK_PATH + 'results.xml')
        root = dom.documentElement
        ts = root.getElementsByTagName('testsuite')
        errors = ts[0].getAttribute("errors")
        tests = ts[0].getAttribute("tests")
        print("失败用例", errors)
        print("总用例", tests)

    def run(self):
        threads = []
        t = threading.Thread(target=self.run_cases, args=(self.tid,))
        threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()
        sleep(2)
        self.save_result()

        task_obj = TestTask.objects.get(id=self.tid)
        task_obj.status = 2  # 更新状态为已完成
        task_obj.save()


if __name__ == '__main__':
    tt = TaskThread(1)
    tt.save_result()
