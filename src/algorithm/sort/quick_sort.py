

def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    pivot = array.pop(0)

    left = quick_sort([x for x in array if x < pivot])
    right = quick_sort([x for x in array if x >= pivot])

    return left + [pivot] + right