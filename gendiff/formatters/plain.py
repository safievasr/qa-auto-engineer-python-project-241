STATUS_REMOVED = "removed"
STATUS_ADDED = "added"
STATUS_CHANGED = "changed"


def to_plain_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, (dict, list)):
        return "[complex value]"
    return str(value)


def format_plain(diff):
    lines = []
    for key, node in diff.items():
        status = node["status"]
        if status == STATUS_REMOVED:
            lines.append(f"Property '{key}' was removed")
        elif status == STATUS_ADDED:
            value = to_plain_value(node["value"])
            lines.append(f"Property '{key}' was added with value: {value}")
        elif status == STATUS_CHANGED:
            old = to_plain_value(node["old_value"])
            new = to_plain_value(node["new_value"])
            lines.append(f"Property '{key}' was updated. From {old} to {new}")
    return "\n".join(lines)