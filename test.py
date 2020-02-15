#!/bin/python3
import os, sys, subprocess, io

if len(sys.argv) <= 1:
    print("Need to provide an input file!")
    quit(1)


def info(*value):
    print("[INFO]:", *value)


project_dir = os.path.dirname(os.path.realpath(__file__))
file_path, ext = os.path.splitext(os.path.realpath(sys.argv[1]))
filename = os.path.basename(file_path)
output_file = os.path.join(project_dir, 'bin', filename,
                           ('Main' if ext == '.java' else 'main') + ext)
classpath = os.path.join(project_dir, 'bin', os.path.basename(file_path))
binary_file = os.path.join(project_dir, 'bin', os.path.basename(file_path),
                           'out')
test_path = os.path.realpath(sys.argv[2]) if len(sys.argv) > 2 else None

info("Project directory: " + project_dir)
info("      Output file: " + output_file)
info("        Classpath: " + classpath) if ext == '.java' else \
info("      Binary file: " + binary_file)
info("        File path: " + file_path + ext)
info("        File name: " + filename)
info("        Extension: " + ext)

info()

if not os.path.exists(os.path.dirname(output_file)):
    os.makedirs(os.path.dirname(output_file))

with open(file_path + ext) as f:
    txt = f.read()

with open(output_file, 'w') as f:
    f.write(txt)

info("Compiling code...")
if ext == ".java":
    subprocess.run(['javac', output_file, '-d', classpath])
elif ext == ".cpp":
    subprocess.run(['g++', '-o', binary_file, output_file])
elif ext == ".c":
    subprocess.run(['gcc', '-o', binary_file, output_file])

command = ['java', '-classpath', classpath, "Main"
           ] if ext == '.java' else [binary_file]


def test_command(command, test_file):
    was_str = isinstance(test_file, str)
    if was_str:
        test_file_path = test_file
        test_file = open(test_file)
    result = subprocess.run(command,
                            stdin=test_file,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    if not was_str:
        return True

    test_file.close()
    test_file_name = os.path.basename(test_file_path)

    answer = result.stdout.decode('utf-8')
    with open(test_file_path + '-ans') as f:
        correct_answer = f.read()

    if answer == correct_answer:
        info("Test case " + test_file_name + " passed")
        return True
    else:
        info("Test case `" + test_file_name + "` failed with input:")
        with open(test_file_path) as f:
            input_data = f.read()
        info("::START INPUT::")
        for line in input_data.split('\n'):
            info(line)
        info("::END INPUT::")
        info("...with output:")
        info("::START OUTPUT::")
        for line in answer.split('\n'):
            info(line)
        info("::END OUTPUT::")
        info("when correct output was:")
        info("::START OUTPUT::")
        for line in correct_answer.split('\n'):
            info(line)
        info("::END OUTPUT::")
        return False


info("Command is: " + str(command))
if test_path is None:
    info("Input file: stdin")
    subprocess.run(command, stdin=sys.stdin, stdout=sys.stdout)
elif os.path.isdir(test_path):
    info("Input folder: " + test_path)
    passing = []
    failing = []
    info()

    for file in os.listdir(test_path):
        if file.endswith('ans'):
            continue
        info("Found input file: " + file)

        to_add = passing if test_command(command, os.path.join(
            test_path, file)) else failing
        to_add.append(file)
        info()

    info("Passed test cases: " + str(passing))
    info("Failed test cases: " + str(failing))

else:
    info("Input file: " + test_path)
    test_command(command, os.path.join(test_path))
