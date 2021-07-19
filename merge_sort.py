def merge_sort(list: list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    Divide: Find the midpoint aof the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list: list) -> list:
    """
    Divide the unsorted list at the midpoint into sublists
    Returns two sublist - left and right
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left: list, right: list) -> list:
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """
    new_l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_l.append(left[i])
            i += 1
        else:
            new_l.append(right[j])
            j += 1

    while i < len(left):
        new_l.append(left[i])
        i += 1

    while j < len(right):
        new_l.append(right[j])
        j += 1

    return new_l


def verify_sorted(list: list) -> bool:
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


a_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]
print(verify_sorted(a_list))
sort_l = merge_sort(a_list)
print(sort_l)
print(verify_sorted(sort_l))