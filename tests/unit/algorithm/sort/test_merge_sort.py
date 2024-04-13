import pytest
from src.algorithm.sort.merge_sort import merge_sort


@pytest.mark.parametrize(
    'array, expected',
    [
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([2, 1, 4, 5, 9, 10, 6], [1, 2, 4, 5, 6, 9, 10]),
        ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50]),
        ([5, 2, 4, 1, 3], [1, 2, 3, 4, 5]),
        ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7])
    ]
)
def test_merge_sort(array, expected):
    sorted = merge_sort(array)
    assert sorted == expected