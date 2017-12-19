from __future__ import print_function
import re
import os
import time as time


def getFileNames(path):
    """
    get files name from the path and return a list of names or [] if path is empty or Error occered
    """
    file_name_list = os.listdir(path)
    return file_name_list


def getTheStuNames(stu_names, file_names):
    """
    get the student names who didn't submit the homework
    return a set of student names or a set() if all submitted
    return a set of duplicated handed names
    """
    submitted_set = set()
    duplicated_set = set()
    file_names = "".join([x for x in file_names if x[0] != '.'])
    for i in stu_names:
        t = len(re.findall(i, file_names))
        if t == 1:
            submitted_set.add(i)
        elif t > 1:
            submitted_set.add(i)
            duplicated_set.add(i)
    res = stu_names - submitted_set
    return res, duplicated_set


if __name__ == "__main__":
    name_set_file_name = "name_set_with_blank_to_separate"
    try:
        print("Loading {0}...".format(name_set_file_name), end='\n')
        with open(name_set_file_name, mode='r', encoding='utf-8') as f:
            s = ' '.join(f.readlines()).split(' ')
            full_name_set = set(s)
            print("Name set is loaded.")
    except FileNotFoundError:
        print("WARNING: \"{0}\" file not found, using default hard-code name set.".format(name_set_file_name), end='\n\n')
        full_name_set = set([
            # MARK: Here to insert your names
        ])
    while True:
        path = input("请输入作业文件夹的路径：")
        print()
        path = path.strip()
        t = time.time()
        try:
            file_names = getFileNames(path)
            result, duplicated = getTheStuNames(full_name_set, file_names)
            if 0 == len(result):
                print("作业已收齐。")
            elif len(full_name_set) == len(result):
                print("没有找到任何人的作业，请检查文件路径是否正确。")
            else:
                print("============================= 未交作业：{0:>2} =============================".format(len(result)))
                for i in result:
                    print(i, end=' ')
                print()
            if 0 < len(duplicated):
                print("============================= 发现重复提交 =============================")
                for i in duplicated:
                    print(i, end=' ')
                print()
            print("========================================================================")
        except FileNotFoundError as e:
            print("Error: {0}".format(e))
        except NotADirectoryError as e:
            print("Error: {0}".format(e))
            print("WARNING: This is not a directory, please input a directory rather than a shortcut link or something...")
        print("Exec time is %5.3f ms" % (1000 * (time.time() - t)))
        print()
