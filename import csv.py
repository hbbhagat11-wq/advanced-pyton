import csv
import json


def read_csv(filename):
    with open(filename, "r") as file:
        data = list(csv.DictReader(file))
    return data


def write_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def convert_csv_to_json(input_file, output_file):
    data = read_csv(input_file)
    write_json(data, output_file)
    return len(data)


if __name__ == "__main__":

    input_file = "students.csv"
    output_file = "students.json"

    count = convert_csv_to_json(input_file, output_file)

    print("CSV to JSON conversion successful!")
    print("Rows converted:", count)
    print("Output file:", output_file)