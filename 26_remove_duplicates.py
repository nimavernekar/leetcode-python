def remove_duplicates(lst):
    """
    Remove duplicates but keep order.
    Example: [1, 2, 2, 3, 1] -> [1, 2, 3]
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]


"""
def remove_duplicates_sorted(lst):
    if not lst:
        return 0

    slow = 0
    for fast in range(1, len(lst)):
        if lst[fast] != lst[slow]:
            slow += 1
            lst[slow] = lst[fast]
    return lst[:slow+1]

print(remove_duplicates_sorted([1,1,2,2,3]))  # [1,2,3]
"""
