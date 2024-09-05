def edit_distance(source: str, target: str) -> int:
    if not len(source):
        return len(target)
    elif not len(target):
        return len(source)

    delta = int(source[-1] != target [-1])

    return min(edit_distance(source[:-1], target[:-1])+delta, edit_distance(source, target[:-1])+1, edit_distance(source[:-1], target)+1)

print(edit_distance("GATTICC", "GALTICC"))