import re

def urlify(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a plus (gumtree standard)
    s = re.sub(r"\s+", '+', s)

    return s