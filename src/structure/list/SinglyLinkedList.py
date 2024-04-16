from typing import Any

class Node:
  
    def __init__(self, data: Any):
        self.data = data
        self.next: Node = None


class SinglyLinkedList:
  
    def __init__(self):
        self.head: Node = None


    def is_empty(self) -> bool:
        return self.head is None


    def length(self) -> int:
        length = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            length += 1
        return length


    def append(self, data: Any) -> None:
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        current_node: Node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node


    def reverse(self) -> None:
        if self.is_empty():
            return
        
        prev_node = None
        current = self.head
        while current is not None:
            next_temp = current.next
            current.next = prev_node
            prev_node = current
            current = next_temp
        self.head = prev_node


