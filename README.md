# aps-test-cases
Test cases for APS

## Using the test runner
Use `python3 test.py <source_file> <test_path>` to run the test runner, and get more
help by using `python3 test.py --help`.

On Windows computers with python3 installed via traditional installer (not the
Microsoft store), use `python` instead of `python3`

### Output of Main File
The test runner compiles your code and runs it; before compiling, it first copies
your code into a file called `.build/Main.ext` where `ext` is the extension of your
program, and the `.build` folder is located in the same directory as the test
runner. Because of this, you can name your file whatever you want; if you're using
Java, you can name your file `Polish.java` and have a main class called `Main` in
that file, and it'll work both with the runner and with Gradescope.

### Examples
#### Standard Input
If your source file is at `/home/aliu/code/aps/hw3/Polish.java`

```
python3 test.py /home/aliu/code/aps/hw3/Polish.java
```

will compile the program and run it using standard input. You'll have the option
to save your run as a test case. If you say yes, you'll ge this prompt:

```
Where should this test case by stored?
```

**You can use tab completion here;** one tab completes, two tabs will suggest possible
values.

#### Single Test Case
You can compile and run the program on a test case by using:

```
python3 test.py /home/aliu/code/aps/hw3/Polish.java hw3/polish/example-1
```

This will run the test case `example-1` and check it against the contents of the
file `example-1-ans` in the same directory.

#### Folder of Test Cases
You can compile and run the program using a folder of test cases by doing:

```
python3 test.py /home/aliu/code/aps/hw3/Polish.java hw3/polish
```

This will run all the test cases in the folder `polish` and check them against
given answers in the folder.
