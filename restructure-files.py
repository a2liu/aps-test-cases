#!/usr/bin/python3
import os, sys

folder_path = os.path.realpath(sys.argv[1])
for name in os.listdir(folder_path):
    path = os.path.join(folder_path, name)
    if os.path.isdir(path) and name.isdigit():
        input_path = os.path.join(path, 'input')
        output_path = os.path.join(path, 'output')
        test_case_path = os.path.join(folder_path, 'test-case-' + name)
        os.rename(input_path, test_case_path)
        os.rename(output_path, itest_case_path + '-ans')
