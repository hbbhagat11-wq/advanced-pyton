def count_lines(path):
    with open(path, "r") as f:
        return sum(1 for _ in f)


def extract_first_lines(path, n):
    lines = []

    with open(path, "r") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line)

    return lines


def write_lines(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)


input_file = "input.txt"
output_file = "output_first_two_lines.txt"

total = count_lines(input_file)
first_two = extract_first_lines(input_file, 2)
write_lines(output_file, first_two)

print("Total lines:", total)
print("First 2 lines extracted successfully.")