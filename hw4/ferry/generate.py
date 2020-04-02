import random, os, sys

test_dir = os.path.dirname(os.path.realpath(__file__))

time_step_limit = 12

step_chance = .99


def random_step():
    return int(time_step_limit * random.random())


def step_forwards():
    return random.random() < step_chance


def generate_test_case(n, t, m):
    lines = [f"{n} {t} {m}"]
    time = 0
    for i in range(0, m):
        if step_forwards():
            time += random_step()
        lines.append(f"{time} {random.choice(['left','right'])}")
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

    txt = generate_test_case(int(sys.argv[1]), int(sys.argv[2]),
                             int(sys.argv[3]))
    file = os.path.join(test_dir, f"test-case-{max_case + 1}")
    with open(file, 'w') as f:
        f.write(txt)


if __name__ == "__main__":
    main()
