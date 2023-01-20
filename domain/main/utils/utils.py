from typing import List


def generate_markdown_array(column_names: List[str], columns_values: List[List[str]]) -> str:
    text = ""
    # Add column names
    text += "|"
    for name in column_names:
        text += f" {name} |"
    text += '\n'
    # Add separator line
    text += "|"
    for _ in column_names:
        text += "------|"
    text += '\n'
    # Add column values
    for row in columns_values:
        text += "|"
        for value in row:
            text += f" {value} |"
        text += '\n'
    return text
