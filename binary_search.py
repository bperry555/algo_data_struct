from typing import Optional


def binary_search(list: list, target: int) -> Optional[int]:
    """
    Binary Search Algorithm
    -Only use on a SORTED list
    O(Log N)
    Constant Space
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def recursive_binary_search(list: list, target: int) -> bool:
    """
    Recursive implimentation of binary search
    """
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(index: Optional[int]):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


def verify_recursion(index: Optional[int]):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 8)
verify(result)
verify_recursion(result)
