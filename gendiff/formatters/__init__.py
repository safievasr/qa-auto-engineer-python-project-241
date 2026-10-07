from gendiff.formatters.stylish import format_stylish

FORMATTERS = {
    "stylish": format_stylish,
}


def get_formatter(name):
    if name not in FORMATTERS:
        raise ValueError(f"Unknown format: {name}")
    return FORMATTERS[name]