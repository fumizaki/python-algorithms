from typing import Any

class Node:

    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value
        self.left: Node = None
        self.right: Node = None

class BinarySearchTree:


    def __init__(self):
        self.root = None


    def insert(self, key: str, value: Any):

        def _insert(node: Node, key: str, value: Any):
            if node is None:
                return Node(key, value)
            
            elif key < node.key:
                node.left = _insert(node.left, key, value)

            else:
                node.right = _insert(node.right, key, value)

            return node

        self.root = _insert(self.root, key, value)


    def search(self, key: str):

        def _search(node: Node, key: str):
            if node is None:
                return None
            
            elif key < node.key:
                return _search(node.left, key)
            
            elif key > node.key:
                return _search(node.right, key)
            
            else:
                return node

        return _search(self.root, key)


    

    



