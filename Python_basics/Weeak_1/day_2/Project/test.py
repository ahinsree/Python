

def binary_search(list, item):
    """
    Performs a binary search on a sorted list to find the index of an item.

    Args:
        search_list: A sorted list of items.
        item: The item to search for in the list.

    Returns:
        The index of the item if found, otherwise None.
    """
    low = 0
    high = len(list) - 1  # Corrected: Used minus sign instead of em-dash

    while low <= high:
        mid = (low + high) // 2  # Corrected: Calculated the middle index properly
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9))    # => 1. Corrected: Python 3 print syntax
print(binary_search(my_list, -1))   # => None. Corrected: Python 3 print syntax