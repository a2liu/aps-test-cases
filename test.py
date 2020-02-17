#!/usr/bin/python3
import os, sys, subprocess, io


def debug(*value):
    print("[DEBUG]:", *value)


if '--help' in sys.argv or '-h' in sys.argv:
    print("""
Hi! This is a test runner for APS. The arguemnts are:

./test.py [--debug] [--help] [-h] <source_file> <test_path>
  source_file   The source file.
  test_path     OPTIONAL. The path for test data. It can be a folder or file.
                If a test case file is named `test-case-1`, this script will look
                for a file in the same folder with the name `test-case-1-ans`
  --help,-h     OPTIONAL. Show this message.
  --debug       OPTIONAL. Show debug information.

Please note that this program can't test for presentation errors! However, it
will tell you what the output should have been, so that should help.
""")
    quit(0)

if '--debug' in sys.argv:
    info = debug
    sys.argv.remove('--debug')
else:
    info = lambda *x: None

assert_correct = False
if '--assert' in sys.argv:
    print("In assertion mode. Test case answers will be written to.")
    sys.argv.remove('--assert')
    assert_correct = True

if len(sys.argv) <= 1:
    print("Need to provide an input file!")
    quit(1)

file_path, ext = os.path.splitext(os.path.realpath(sys.argv[1]))
output_file_basename = ('Main' if ext == '.java' else 'main') + ext
project_dir = os.path.dirname(os.path.realpath(__file__))
bin_dir = os.path.join(project_dir, 'bin')
filename = os.path.basename(file_path)
output_file = os.path.join(bin_dir, filename, output_file_basename)
classpath = os.path.join(bin_dir, os.path.basename(file_path))
binary_file = os.path.join(bin_dir, os.path.basename(file_path), 'out')
test_path = os.path.realpath(sys.argv[2]) if len(sys.argv) > 2 else None

info("Project directory: " + project_dir)
info(" Output directory: " + bin_dir)
info("  Output basename: " + output_file_basename)
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

with open(os.path.join(bin_dir, output_file_basename), 'w') as f:
    f.write(txt)

print("Compiling code...")
if ext == ".java":
    result = subprocess.run(['javac', output_file, '-d', classpath])
elif ext == ".cpp":
    result = subprocess.run(['g++', '-o', binary_file, output_file])
elif ext == ".c":
    result = subprocess.run(['gcc', '-o', binary_file, output_file])

if result.returncode != 0:
    exit(1)

command = ['java', '-classpath', classpath, "Main"
           ] if ext == '.java' else [binary_file]
info("Command is: " + str(command))


def print_value_red(value, title=None):
    if title is not None:
        print("\033[1m" + title + "\033[0m\033[31m")
    for line in value.split('\n'):
        print(line)
    print("\033[0m", end='')


def print_value(value, title=None):
    if title is not None:
        print("\033[1m" + title + "\033[0m")
    print("::START::")
    for line in value.split('\n'):
        print(line)
    print("::END::")


def test_command(command, test_file):
    test_file_path = test_file
    if isinstance(test_file, str):
        test_file_path = test_file
        test_file = open(test_file)

    result = subprocess.run(command,
                            stdin=test_file,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    test_file.close()
    answer = result.stdout.decode('utf-8').strip()
    err = result.stderr.decode('utf-8').strip()

    if not os.path.exists(test_file_path + '-ans') or assert_correct:
        if assert_correct:
            with open(test_file_path + '-ans', 'w') as f:
                f.write(answer.strip())
                f.write('\n')
        else:
            info("Couldn't find answer file")

        print_value(answer, title=f"Program had output:")
        if err.strip() != "":
            print_value_red(err, title="with stderr:")
        return

    test_file_name = os.path.basename(test_file_path)
    with open(test_file_path + '-ans') as f:
        correct_answer = f.read().strip()

    if answer == correct_answer:
        print("Test case `" + test_file_name + "` passed")
        return True
    else:
        with open(test_file_path) as f:
            input_data = f.read().strip()
        print_value(input_data,
                    title=f"Test case `{ test_file_name }` failed with input:")
        print_value(answer, title=f"...with output:")
        print_value(correct_answer, title=f"when correct output was:")
        if err.strip() != "":
            print_value_red(err, title="with stderr:")
        return False


if test_path is None:
    print("Input file: stdin")
    print("Use Ctrl-D to end input")
    temp_path = os.path.join(project_dir, 'bin', ".tmp")
    txt = sys.stdin.read()
    with open(temp_path, 'w') as f:
        f.write(txt)
    with open(temp_path) as f:
        test_command(command, f)
    user_input = input("Save this run as a test case? [y/n] ")
    if user_input.startswith('y'):
        test_case_path = input("Where should the test case be stored?")
        print(
            "Please store the answer to this test case at the following path:\n"
            + test_case_path + '-ans')

elif os.path.isdir(test_path):
    print("Input folder: " + test_path)
    passing = []
    failing = []
    info()

    for file in os.listdir(test_path):
        if file.endswith('ans') or file.startswith('.') or file.endswith(
                '.py'):
            continue
        info("Found input file: " + file)

        if test_command(command, os.path.join(test_path, file)):
            passing.append(file)
        else:
            failing.append(file)

    print("Passed test cases: " + str(passing))
    print("Failed test cases: " + str(failing))

else:
    print("Input file: " + test_path)
    test_command(command, os.path.join(test_path))
