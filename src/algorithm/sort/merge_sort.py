

def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

    
def merge(left: list, right: list) -> list:
    merged = []
    left_i = 0
    right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            merged.append(left[left_i])
            left_i += 1
        else:
            merged.append(right[right_i])
            right_i += 1

    if left_i < len(left):
        merged.extend(left[left_i:])
    if right_i < len(right):
        merged.extend(right[right_i:])

    return merged