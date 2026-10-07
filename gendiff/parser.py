import json
import os

import yaml


def read_file(filepath):
    with open(filepath) as f:
        return f.read()


def get_format(filepath):
    _, ext = os.path.splitext(filepath)
    return ext.lstrip(".").lower()


def parse(content, fmt):
    if fmt == "json":
        return json.loads(content)
    if fmt in ("yaml", "yml"):
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported format: {fmt}")


def parse_file(filepath):
    return parse(read_file(filepath), get_format(filepath))