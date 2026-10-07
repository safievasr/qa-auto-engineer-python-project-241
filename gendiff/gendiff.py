from gendiff.formatters import get_formatter
from gendiff.parser import parse_file

REMOVED = "removed"
ADDED = "added"
UNCHANGED = "unchanged"
CHANGED = "changed"

DEFAULT_FORMAT = "stylish"


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}
    for key in keys:
        if key not in data2:
            diff[key] = {"status": REMOVED, "value": data1[key]}
        elif key not in data1:
            diff[key] = {"status": ADDED, "value": data2[key]}
        elif data1[key] == data2[key]:
            diff[key] = {"status": UNCHANGED, "value": data1[key]}
        else:
            diff[key] = {
                "status": CHANGED,
                "old_value": data1[key],
                "new_value": data2[key],
            }
    return diff


def generate_diff(filepath1, filepath2, format_name=DEFAULT_FORMAT):
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)