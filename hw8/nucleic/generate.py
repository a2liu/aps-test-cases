import random, os, sys

test_dir = os.path.dirname(os.path.realpath(__file__))


def generate_test_case(length, n):
    lines = [length + " " + n
             ]  # I'd like to use an f-string, but compat man, compat

    length, n = int(length), int(n)
    lines.extend(''.join(random.choices("ACGT", k=length)) for x in range(n))
    return '\n'.join(lines)


def main():
    max_case = 0
    for file in os.listdir(test_dir):
        name_chunks = file.split('-')
        if len(name_chunks) != 3:
            continue
        if name_chunks[0] != 'test':
            continue
        if name_chunks[1] != 'case':
            continue

        case_num = int(name_chunks[2])
        if max_case < case_num:
            max_case = case_num

    txt = generate_test_case(sys.argv[1], sys.argv[2])
    file = os.path.join(test_dir, f"test-case-{max_case + 1}")
    with open(file, 'w') as f:
        f.write(txt)


if __name__ == "__main__":
    main()
