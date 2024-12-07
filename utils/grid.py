def load_from_string(s: str) -> list[list[str]]:
    return [list(line) for line in s.strip().split('\n')]

