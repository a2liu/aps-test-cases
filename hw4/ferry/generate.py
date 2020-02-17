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
    for file in os.listdir(test_dir):
        name_chunks = file.split('-')
        max_case = 1
        if len(name_chunks) == 3 and name_chunks[0] == 'test' and name_chunks[
                1] == 'case':
            case_num = int(name_chunks[2])
            if max_case < case_num:
                max_case = case_num

        with open(os.path.join(test_dir, f"test-case-{max_case + 1}"),
                  'w') as f:
            f.write(
                generate_test_case(int(sys.argv[1]), int(sys.argv[2]),
                                   int(sys.argv[3])))


if __name__ == "__main__":
    main()
