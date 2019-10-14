"""
author: zhiheng
function: 公共功能的方法
"""
import os


def sort_file_by_time(file_path):
    """
    将目录下面的所有文件按照时间进行排序
    """
    files = os.listdir(file_path)
    if not files:
        return
    else:
        files = sorted(files, key=lambda x: os.path.getmtime(
            os.path.join(file_path, x)))
        return files
