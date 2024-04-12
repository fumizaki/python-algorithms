
def binary_search(sequence: list, target: int) -> int:
    """
    計算量: O(log n)
    """
    left = 0
    right = len(sequence) - 1
    while left <= right:
        mid = (left + right) // 2
        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1