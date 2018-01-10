from __future__ import print_function
import re
import os


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


def print_result(result, duplicated, max_length):
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
    title_bar = '============================='
    if 0 == len(result):
        print("作业已收齐。")
    elif max_length == len(result):
        print("没有找到任何人的作业，请检查文件路径是否正确。")
    else:
        print("{0} 未交作业：{1:>2} {0}".format(title_bar, len(result)))
        t = 0
        for index in range(len(result)):
            print(result[index], end=' ')
            t += 2*len(result[index])+1
            if ((len(title_bar)*2)+len(' 未交作业：00 ')) - (t % ((len(title_bar)*2)+len(' 未交作业：00 '))) < 7:
                print('\n', end='')
        print()
    if 0 < len(duplicated):
        print("{0} 发现重复提交 {0}".format(title_bar))
        for i in duplicated:
            print(i, end=' ')
        print()
    print("========================================================================", end='\n\n')


if __name__ == "__main__":
    name_set_file_name = "name_set"
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
    while True:
        path = input("请输入作业文件夹的路径：")
        print()
        path = path.strip()
        try:
            file_names = get_file_names(path)
            result, duplicated = get_the_student_names(full_name_set, file_names)
        except FileNotFoundError as e:
            print("错误：找不到文件或目录：{0}".format(e.filename), end='\n\n')
            continue
        except NotADirectoryError as e:
            print("错误：这不是一个目录：{0}".format(e.strerror), end='\n\n')
            continue
        print_result(result, duplicated, len(full_name_set))
