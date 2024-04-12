import pytest
from src.algorithm.search.binary_search import binary_search


@pytest.mark.parametrize(
    'sequence, target, expected',
    [
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7], 2, 1),
        ([1, 2, 3, 4, 5, 6, 7], 3, 2),
        ([1, 2, 3, 4, 5, 6, 7], 4, 3),
        ([1, 2, 3, 4, 5, 6, 7], 5, 4),
        ([1, 2, 3, 4, 5, 6, 7], 6, 5),
        ([1, 2, 3, 4, 5, 6, 7], 7, 6),
        ([1, 2, 3, 4, 5, 6, 7], 8, -1),
    ]
)
def test_binary_search(sequence, target, expected):
    index = binary_search(sequence, target)
    assert index == expected