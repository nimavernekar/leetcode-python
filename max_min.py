def find_max_min(lst):
    if not lst:
        return None, None

    maximum = minimum = lst[0]
    for num in lst[1:]:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    return maximum, minimum

print(find_max_min([2, 7, 1, 9, 3]))  # (9, 1)
