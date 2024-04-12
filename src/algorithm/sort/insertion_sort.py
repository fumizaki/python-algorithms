

def insertion_sort(array: list) -> list:
    """
    計算量
    * 最良の場合: O(n)
        - 入力データが既にソートされている場合に最良となる

    * 最悪の場合: O(n^2)
        - 入力データが降順に並んでいる場合に最悪となる
        
    * 平均の場合: O(n^2)

    """
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1

        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = value

    return array

