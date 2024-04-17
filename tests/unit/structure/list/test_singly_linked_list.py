import pytest
from src.structure.list.SinglyLinkedList import SinglyLinkedList


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


def test_reverse_recursive_with_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.reverse_recursive()
    assert linked_list.head is None


def test_reverse_recursive_with_single_element_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.reverse_recursive()
    assert linked_list.head.data == 10
    assert linked_list.head.next is None


def test_reverse_recursive_with_multiple_elements_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.reverse_recursive()
    current_node = linked_list.head
    assert current_node.data == 30
    assert current_node.next.data == 20
    assert current_node.next.next.data == 10
    assert linked_list.head.next.next.next is None


def test_remove_from_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.remove(10)
    assert linked_list.head is None


def test_remove_first_element_from_non_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.remove(10)
    assert linked_list.head.data == 20
    assert linked_list.head.next is None


def test_remove_middle_element_from_non_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.remove(20)
    current_node = linked_list.head
    assert current_node.data == 10
    assert current_node.next.data == 30
    assert current_node.next.next is None


def test_remove_last_element_from_non_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.remove(30)
    current_node = linked_list.head
    assert current_node.data == 10
    assert current_node.next.data == 20
    assert current_node.next.next is None


def test_remove_non_existent_element():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.remove(30)
    current_node = linked_list.head
    assert current_node.data == 10
    assert current_node.next.data == 20
    assert current_node.next.next is None




