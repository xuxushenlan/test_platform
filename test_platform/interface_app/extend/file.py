import os


# 创建目录
def mkdir(path):
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
        return True
    else:
        return False


if __name__ == '__main__':
    mkdir("D:/git/test_platform/test_platform/resource/tasks/1")
