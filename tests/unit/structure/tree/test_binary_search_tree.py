from src.structure.tree.BinarySearchTree import BinarySearchTree

def test_insert_empty_tree():
  """
  Test inserting a key-value pair into an empty tree
  """
  tree = BinarySearchTree()
  tree.insert("apple", "red")
  assert tree.root.key == "apple"
  assert tree.root.value == "red"

def test_insert_existing_key():
  """
  Test inserting a key-value pair with an existing key
  """
  tree = BinarySearchTree()
  tree.insert("apple", "red")
  # Attempt to insert the same key with a different value
  tree.insert("apple", "green")
  # Search for the original value
  found_node = tree.search("apple")
  assert found_node.value == "red"

def test_insert_left_child():
  """
  Test inserting a key-value pair smaller than the root
  """
  tree = BinarySearchTree()
  tree.insert("banana", "yellow")
  tree.insert("apple", "red")
  assert tree.root.left.key == "apple"
  assert tree.root.left.value == "red"

def test_insert_right_child():
  """
  Test inserting a key-value pair larger than the root
  """
  tree = BinarySearchTree()
  tree.insert("apple", "red")
  tree.insert("banana", "yellow")
  assert tree.root.right.key == "banana"
  assert tree.root.right.value == "yellow"

def test_search_existing_key():
  """
  Test searching for a key-value pair that exists in the tree
  """
  tree = BinarySearchTree()
  tree.insert("apple", "red")
  found_node = tree.search("apple")
  assert found_node.key == "apple"
  assert found_node.value == "red"

def test_search_missing_key():
  """
  Test searching for a key-value pair that does not exist in the tree
  """
  tree = BinarySearchTree()
  tree.insert("apple", "red")
  found_node = tree.search("banana")
  assert found_node is None