import json
import os


def read_file(filepath):
    with open(filepath) as f:
        return f.read()


def get_format(filepath):
    _, ext = os.path.splitext(filepath)
    return ext.lstrip(".").lower()


def parse(content, fmt):
    if fmt == "json":
        return json.loads(content)
    raise ValueError(f"Unsupported format: {fmt}")


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return value
    return json.dumps(value)


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    lines = []
    for key in keys:
        if key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {format_value(data1[key])}")
        else:
            lines.append(f"  - {key}: {format_value(data1[key])}")
            lines.append(f"  + {key}: {format_value(data2[key])}")
    body = "\n".join(lines)
    return "{\n" + body + "\n}"


def generate_diff(filepath1, filepath2):
    data1 = parse(read_file(filepath1), get_format(filepath1))
    data2 = parse(read_file(filepath2), get_format(filepath2))
    return build_diff(data1, data2)