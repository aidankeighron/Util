def iterating_through_submasks(mask: int) -> list:
    all_submasks = []
    submask = mask
    while submask:
        all_submasks.append(submask)
        submask = (submask - 1) & mask

    return all_submasks
print(iterating_through_submasks(15))