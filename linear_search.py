from typing import Optional


def linear_search(list: list, target: int) -> Optional[int]:
    """
    Returns the first index position of the targe if found, else returns None.
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def linear_search_2(list: list, target: int) -> Optional[int]:
    """
    Another more Pythonic way to code linear search.
    """
    for i in list:
        if i == target:
            return list.index(i)
    return None


def verify(index: Optional[int]):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 7)
verify(result)

result = linear_search_2(numbers, 15)
verify(result)

result = linear_search_2(numbers, 7)
verify(result)
