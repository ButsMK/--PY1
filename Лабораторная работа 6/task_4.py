import json
import csv

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE) -> list[dict]:
    # TODO реализовать конвертер из csv в json
    with open(INPUT_FILE) as f:
        lines = [line for line in f]
    for i, line in enumerate(lines):
        lines[i] = line.replace('"', '').replace('\n', '')
    head = lines[0].split(',')
    other = lines[1:]
    out_dict = [{head[i]:other[j].split(',')[i] for i in range(len(head))} for j in range(len(other))]
    return out_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
