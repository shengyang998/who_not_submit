from __future__ import print_function
import re
import os
import sys


def get_file_names(path):
    """
    get files name from the path and return a list of names or [] if path is empty or Error occered
    """
    file_name_list = os.listdir(path)
    return file_name_list


def get_the_student_names(stu_names, file_names):
    """
    get the student names who didn't submit the homework
    return a set of student names or a set() if all submitted
    return a set of duplicated submition names
    return a set of submitted names
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
    return res, duplicated_set, submitted_set


def print_result(result, duplicated, submitted, max_length):
    """
    print the result of whom not submit the homework
    :param result: a set including the names who didn't submit the homework, can be None
    :param duplicated: a set including the names who didn't submit the homework and who is duplicated, can be None
    :return: None
    """
    if isinstance(result, set):
        result = list(result)
    if isinstance(duplicated, set):
        duplicated = list(duplicated)
    if isinstance(submitted, set):
        submitted = list(submitted)
    title_bar = '============================='
    if 0 == len(result):
        print("作业已收齐。")
    elif max_length == len(result):
        print("没有找到任何人的作业，请检查文件路径是否正确。")
    else:
        title = "{0} 未交作业：{1:>2} {0}".format(title_bar, len(result))
        print(title)
        print_names(result, len(title))
        title = "{0} 已交作业：{1:>2} {0}".format(title_bar, len(submitted))
        print(title)
        print_names(submitted, len(title))
        if 0 < len(duplicated):
            title = "{0} 发现重复提交 {0}".format(title_bar)
            print(title)
            print_names(duplicated, len(title))
        print('=' * (len(title) + 5), end='\n')
    print()


def print_names(result, title_bar_len):
    cur_length = 0
    flag_to_return = 0
    for index in range(len(result)):
        print(result[index], end=' ')
        flag_to_return += 1
        cur_length += 2 * len(result[index]) + 1
        if title_bar_len - (cur_length % title_bar_len) < 5 and flag_to_return > 1:
            print("\n", end='')
            flag_to_return = 0
    print("\n", end='')


def main(path=None):
    dir_to_self = os.path.split(os.path.realpath(sys.argv[0]))[0] + '/'
    name_set_file_name = dir_to_self + "name_set"
    try:
        print("正在读取 {0}...".format(name_set_file_name), end='\n')
        with open(name_set_file_name, mode='r', encoding='utf-8') as f:
            s = ' '.join(f.readlines()).split(' ')
            full_name_set = set(s)
            print("{0} 读取成功".format(name_set_file_name))
    except FileNotFoundError:
        print("警告: 未找到 \"{0}\" 文件，将使用硬编码的名字集合...".format(name_set_file_name), end='\n\n')
        full_name_set = set([
            # MARK: Here to insert your names
        ])
        if len(full_name_set) == 0:
            print("错误：名字集合为空，程序将退出。")
            exit()
    while True:
        if path is None:
            path = input("请输入作业文件夹的路径：")
        print()
        path = path.strip()
        try:
            file_names = get_file_names(path)
            result, duplicated, submitted = get_the_student_names(full_name_set, file_names)
        except FileNotFoundError as e:
            print("错误：找不到文件或目录：{0}".format(e.filename), end='\n\n')
            path = None
            continue
        except NotADirectoryError as e:
            print("错误：这不是一个目录：{0}".format(e.strerror), end='\n\n')
            path = None
            continue
        print_result(result, duplicated, submitted, len(full_name_set))
        path = None


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            main(sys.argv[1])
        else:
            main()
    except KeyboardInterrupt as e:
        print("\nAccept Ctrl + C. The program will be exit. ")
        exit()
