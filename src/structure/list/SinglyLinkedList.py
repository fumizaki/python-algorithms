from typing import Any, Optional

class Node:
  
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None


class SinglyLinkedList:
  
    def __init__(self):
        self.head: Optional[Node] = None


    def length(self) -> int:
        length = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            length += 1
        return length


    def append(self, data: Any) -> None:
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node: Node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        prev_node: Optional[Node] = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if prev_node is None:
            return

        if current_node is None:
            return
        
        prev_node.next = current_node.next
        current_node = None
    

    def reverse(self) -> None:
        
        prev_node: Optional[Node] = None
        current = self.head

        while current:
            next_temp = current.next
            current.next = prev_node
            prev_node = current
            current = next_temp

        self.head = prev_node


    def reverse_recursive(self) -> None:

        def _reverse(node: Optional[Node], reversed_head: Optional[Node]) -> Optional[Node]:
            
            if node is None:
                return reversed_head

            next_temp = node.next
            node.next = reversed_head
            reversed_head = node
            node = next_temp
            return _reverse(node, reversed_head)

        reversed_head: Optional[Node] = None
        self.head = _reverse(self.head, reversed_head)
