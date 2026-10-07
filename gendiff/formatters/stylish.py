import json

STATUS_REMOVED = "removed"
STATUS_ADDED = "added"
STATUS_UNCHANGED = "unchanged"
STATUS_CHANGED = "changed"


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return value
    return json.dumps(value)


def format_stylish(diff):
    lines = []
    for key, node in diff.items():
        status = node["status"]
        if status == STATUS_REMOVED:
            lines.append(f"  - {key}: {format_value(node['value'])}")
        elif status == STATUS_ADDED:
            lines.append(f"  + {key}: {format_value(node['value'])}")
        elif status == STATUS_UNCHANGED:
            lines.append(f"    {key}: {format_value(node['value'])}")
        elif status == STATUS_CHANGED:
            lines.append(f"  - {key}: {format_value(node['old_value'])}")
            lines.append(f"  + {key}: {format_value(node['new_value'])}")
    body = "\n".join(lines)
    return "{\n" + body + "\n}"