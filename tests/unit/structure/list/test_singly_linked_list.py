import pytest
from src.structure.list.SinglyLinkedList import SinglyLinkedList


def test_is_empty_with_empty_list():
    linked_list = SinglyLinkedList()
    is_empty = linked_list.is_empty()
    assert is_empty == True

def test_is_empty_with_non_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    is_empty = linked_list.is_empty()
    assert is_empty == False

def test_length_with_empty_list():
    linked_list = SinglyLinkedList()
    length = linked_list.length()
    assert length == 0

def test_length_with_non_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    length = linked_list.length()
    assert length == 2

def test_append_with_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    assert linked_list.head.data == 10
    assert linked_list.head.next is None

def test_append_with_non_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    current_node = linked_list.head
    assert current_node.data == 10
    assert current_node.next.data == 20
    assert linked_list.head.next.next is None

def test_reverse_with_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.reverse()
    assert linked_list.head is None

def test_reverse_with_single_element_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.reverse()
    assert linked_list.head.data == 10
    assert linked_list.head.next is None

def test_reverse_with_multiple_elements_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.reverse()
    current_node = linked_list.head
    assert current_node.data == 30
    assert current_node.next.data == 20
    assert current_node.next.next.data == 10
    assert linked_list.head.next.next.next is None