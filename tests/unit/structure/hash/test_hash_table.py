import pytest
from src.structure.hash.HashTable import HashTable

def test_hash_table_init():
    hash_table = HashTable()
    assert hash_table.size == 10
    assert len(hash_table.table) == 10


def test_hash_table_init_fail():
    with pytest.raises(ValueError):
        HashTable(0)

def test_hash_function():
    hash_table = HashTable()
    key1 = "apple"
    key2 = "banana"
    key3 = "cherry"

    index1 = hash_table._hash(key1)
    index2 = hash_table._hash(key2)
    index3 = hash_table._hash(key3)

    assert index1 < hash_table.size and index1 >= 0
    assert index2 < hash_table.size and index2 >= 0
    assert index3 < hash_table.size and index3 >= 0


def test_add_get_delete():
    hash_table = HashTable()
    hash_table.add("apple", 10)
    hash_table.add("banana", 20)
    hash_table.add("banana", 20)
    hash_table.add("cherry", 30, priority=False)
    hash_table.add("orange", 50, priority=False)
    hash_table.add("grape", 60, priority=False)
    hash_table.add("grape", 70, priority=False)

    assert hash_table.get("apple") == 10
    assert hash_table.get("banana") == 20
    assert hash_table.get("cherry") == 30

    hash_table.add("cherry", 40, priority=True)
    assert hash_table.get("cherry") == 40

    hash_table.delete("apple")
    assert hash_table.get("apple") is None

    hash_table.delete("banana")
    assert hash_table.get("banana") is None

    hash_table.delete("cherry")
    assert hash_table.get("cherry") is None