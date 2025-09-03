def reverse_list(lst):
    """
    Reverse the given list without using reverse() or slicing.
    Example: [1, 2, 3] -> [3, 2, 1]
    """
    rev = []
    for item in lst:
      rev = [item] + rev   # put new element in front
    return rev
print(reverse_list([1, 2, 3, 4]))



"""
def reverse_list(lst):
    rev = []
    for i in range(len(lst) - 1, -1, -1):  # loop backwards
        rev.append(lst[i])
    return rev

print(reverse_list([1, 2, 3, 4]))
"""
