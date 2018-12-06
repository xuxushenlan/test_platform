import os
from django.apps import AppConfig
from test_platform.settings import BASE_DIR


class InterfaceAppConfig(AppConfig):
    name = 'interface_app'


# 配置路径
POR_PATH = BASE_DIR.replace('\\', '/')
TASK_RUN_FILE = POR_PATH + "/interface_app/extend/task_run.py"
TASK_PATH = POR_PATH + "/resource/tasks/"


if __name__ == '__main__':
    print(TASK_RUN_FILE)
