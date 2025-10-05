import timeit

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test: Time a list of 1000 elements
setup = "from __main__ import linear_search; arr = list(range(1000)); target = 500"
print(timeit.timeit("linear_search(arr, target)", setup=setup, number=1000))