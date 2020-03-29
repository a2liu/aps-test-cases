# aps-test-cases
Test cases for APS

## Using the test runner
Use `python3 test.py <source_file> <test_path>` to run the test runner, and get more
help by using `python3 test.py --help`.

On Windows computers with python3 installed via traditional installer (not the Microsoft store), use `python` instead of `python3`

#### Output of Main File
The test runner compiles your code and runs it; before compiling, it first copies
your code into this repository in the `bin` directory.

#### Examples

If your source file is at `/home/aliu/code/aps/hw3/Polish.java`

```
python3 test.py /home/aliu/code/aps/hw3/Polish.java
```

will compile the program and run it using standard input. You can compile and run
the program using a folder of test cases by doing:

```
python3 test.py /home/aliu/code/aps/hw3/Polish.java hw3/polish
```

This will run all the test cases in the folder `polish` and check them against
given answers in the folder.
