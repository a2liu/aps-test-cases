import random, os, sys

test_dir = os.path.dirname(os.path.realpath(__file__))


def generate_test_case(length):
    arr = [x for x in range(int(length))]
    random.shuffle(arr)

    final_arr = [str(length)]
    final_arr.extend(str(x) for x in arr)
    return "\n".join(final_arr)


def main():
    max_case = 1
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

    txt = generate_test_case(sys.argv[1])
    file = os.path.join(test_dir, f"test-case-{max_case + 1}")
    with open(file, 'w') as f:
        f.write(txt)


if __name__ == "__main__":
    main()
