#!/usr/bin/python3
import os, sys, subprocess, io, datetime, readline

HELP_TEXT = """
Hi! This is a test runner for APS. The arguemnts are:

python3 test.py [--debug] [--help] [-h] <source_file> <test_path>

  source_file   The source file to compile.
  test_path     OPTIONAL. The path for test data. It can be a folder or file.
                If a test case file is named `test-case-1`, this script will look
                for a file in the same folder with the name `test-case-1-ans`
  --help,-h     OPTIONAL. Show this message.
  --debug       OPTIONAL. Show debug information.

Please note that this program can't test for presentation errors! However, it
will tell you what the output should have been, so that should help.
"""

readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")


def info(*values):
    pass


def print_bold(value, end='\n'):
    if value is not None:
        print("\033[1m" + str(value) + "\033[0m", end=end)


def print_value_red(value, title=None):
    if value is None:
        return
    print_bold(title)
    print("\033[31m", end="")
    for line in value.split('\n'):
        print(line)
    print("\033[0m", end='')


def print_value(value, title=None):
    if value is None:
        return
    print_bold(title)
    print("::START::")
    lines = value.split('\n')
    if len(lines) > 100:
        for i in range(50):
            print(lines[i])
        print("\n...\n")
        for i in range(50):
            print(lines[-i])
    else:
        for line in lines:
            print(line)
    print("::END::")


def run_command(command, test_file):
    start = datetime.datetime.now()
    result = subprocess.run(command,
                            stdin=test_file,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    end = datetime.datetime.now()
    stdout = result.stdout.decode('utf-8').strip()
    stderr = result.stderr.decode('utf-8').strip()
    stderr = None if stderr == "" else stderr
    success = (result.returncode == 0)
    return stdout, stderr, success, (end - start).microseconds / 1000000


def test_command(command, test_file_path, assert_correct=False):
    with open(test_file_path) as f:
        answer, err, success, time_elapsed = run_command(command, f)

    test_file_name = os.path.basename(test_file_path)

    if not os.path.exists(test_file_path + '-ans') or assert_correct:
        if not assert_correct:
            info("Couldn't find answer file")
        else:
            with open(test_file_path + '-ans', 'w') as f:
                f.write(answer)
                f.write('\n')

        print_value(answer,
                    title=f"For `{test_file_name}` program had output:")
        print_value_red(err, title="with stderr:")
        print_bold("...and ran in " + str(time_elapsed) + " seconds\n")
        return success

    with open(test_file_path + '-ans') as f:
        correct_answer = f.read().strip()

    if answer == correct_answer:
        print("Test case `", end='')
        print_bold(test_file_name, end='')
        print("` passed in ", end='')
        print_bold(time_elapsed, end='')
        print(" seconds")
        return True
    else:
        with open(test_file_path) as f:
            input_data = f.read().strip()
        print_value(input_data,
                    title=f"Test case `{ test_file_name }` failed with input:")
        print_value(answer, title=f"with output:")
        print_value(correct_answer, title=f"when correct output was:")
        print_value_red(err, title="with stderr:")
        return False


def main():
    global info
    if '--help' in sys.argv or '-h' in sys.argv:
        return print(HELP_TEXT)

    if '--debug' in sys.argv:
        info = lambda *value: print("[DEBUG]:", *value)
        sys.argv.remove('--debug')

    assert_correct = False
    if '--assert' in sys.argv:
        print("In assertion mode. Test case answers will be written to.")
        sys.argv.remove('--assert')
        assert_correct = True

    just_compile = False
    if '--compile' in sys.argv:
        sys.argv.remove('--compile')
        just_compile = True

    if len(sys.argv) <= 1:
        raise Exception(
            "No program file was given. (should be first argument)")

    file_path, ext = os.path.splitext(os.path.realpath(sys.argv[1]))
    project_dir = os.path.dirname(os.path.realpath(__file__))
    bin_dir = os.path.join(project_dir, '.build')
    filename = os.path.basename(file_path)
    output_filename = 'Main.java' if ext == '.java' else ('main' + ext)
    output_file = os.path.join(bin_dir, filename, output_filename)
    classpath = os.path.join(bin_dir, filename)
    binary_file = os.path.join(bin_dir, filename, 'out')
    test_path = os.path.realpath(sys.argv[2]) if len(sys.argv) > 2 else None

    info("Project directory: " + project_dir)
    info(" Output directory: " + bin_dir)
    info("      Output file: " + output_file)

    info("        Classpath: " + classpath)
    info("      Binary file: " + binary_file)

    info("        File name: " + filename)
    info("        Extension: " + ext)
    info()

    if not os.path.exists(os.path.dirname(output_file)):
        try:
            os.makedirs(os.path.dirname(output_file))
        except Exception as e:
            info(e)

    with open(file_path + ext) as f:
        txt = f.read()

    with open(output_file, 'w') as f:
        f.write(txt)

    with open(os.path.join(bin_dir, output_filename), 'w') as f:
        f.write(txt)

    print("Compiling code...", end='')
    if ext == ".java":
        result = subprocess.run(['javac', output_file, '-d', classpath])
    elif ext == ".cpp":
        result = subprocess.run(['g++', '-o', binary_file, output_file])
    elif ext == ".c":
        result = subprocess.run(['gcc', '-o', binary_file, output_file])

    if result.returncode != 0:
        print()
        return False

    print_bold(" Done.")

    if just_compile:
        return

    command = ['java', '-classpath', classpath, "Main"
               ] if ext == '.java' else [binary_file]
    info("Command is: " + str(command))

    if test_path is None:
        print("Input file: stdin")
        print("Use Ctrl-D to end input (Ctrl-Z + Enter on Windows)")
        temp_path = os.path.join(bin_dir, ".tmp")
        txt = sys.stdin.read()
        with open(temp_path, 'w') as f:
            f.write(txt)
        with open(temp_path) as f:
            answer, err, success, time_elapsed = run_command(command, f)

        print_value(answer, title=f"Program had output:")
        print_value_red(err, title="with stderr:")
        print_bold("...and ran in " + str(time_elapsed) + " seconds")
        if not success:
            return False

        while True:
            try:
                user_input = input("Save this run as a test case? [y/n] ")
            except EOFError as e:
                return print()

            if not user_input.startswith('y'):
                return

            try:
                test_case_path = input(
                    "Where should the test case be stored? ")
            except EOFError as e:
                return print()

            if not os.path.exists(test_case_path):
                break

            print("test case already exists, continue? [y/n] ")
            if user_input.startswith('y'):
                break

        try:
            os.makedirs(os.path.dirname(test_case_path))
        except Exception as e:
            info(e)

        with open(test_case_path, 'w') as f:
            f.write(txt)
        with open(test_case_path + '-ans', 'w') as f:
            f.write(answer.strip())
            f.write('\n')

        print(f"Test case answer was stored at: {test_case_path}-ans")
    elif os.path.isdir(test_path):
        print("Input folder: " + test_path)
        passing = []
        failing = []
        info()

        for file in os.listdir(test_path):
            if file.endswith('ans'):
                continue
            if '.' in file:
                print("Skipping file " + file + "because it has an extension.")
                continue

            info("Found input file: " + file)

            if test_command(command, os.path.join(test_path, file),
                            assert_correct):
                passing.append(file)
            else:
                failing.append(file)

        print("Passed test cases: " + str(passing))
        print("Failed test cases: " + str(failing))
    else:  # testing a single file
        print("Input file: " + test_path)
        test_command(command, os.path.join(test_path), assert_correct)


if __name__ == "__main__":
    try:
        ret_value = main()
        if ret_value is not None:
            exit(1)
    except Exception as e:
        print_bold("Got an error:\n\n    ", e, '\n')
        print("You can use the ", end='')
        print_bold('--help', end='')
        print(" flag to get more information on how to use this test runner.")
