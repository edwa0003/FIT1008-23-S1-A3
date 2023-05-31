""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""

from __future__ import annotations

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev, further modified by Jackson Goerner'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
from node import TreeNode
import sys

# generic types
K = TypeVar('K')
I = TypeVar('I')
T = TypeVar('T')


class BinarySearchTree(Generic[K, I]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the bst is empty
            :complexity: O(1)
        """
        return self.root is None

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: K) -> bool:
        """
        Checks to see if the key is in the BST
        complexity: see __getitem__(self, key: K) -> (K, I)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: K) -> I:
        """
        Attempts to get an item in the tree, it uses the Key to attempt to find it
        complexity best: O(CompK) finds the item in the root of the tree
        complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
        CompK is the complexity of comparing the keys
        """
        return self.get_tree_node_by_key(key).item

    def get_tree_node_by_key(self, key: K) -> TreeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: TreeNode, key: K) -> TreeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        elif key < current.key:
            return self.get_tree_node_by_key_aux(current.left, key)
        else:  # key > current.key
            return self.get_tree_node_by_key_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: TreeNode, key: K, item: I) -> TreeNode:
        """
        Attempts to insert an item into the tree, it uses the Key to insert it

        complexity best: O(CompK) inserts the item at the root.
        complexity worst: O(CompK * D) inserting at the bottom of the tree
        where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = TreeNode(key, item=item)
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
            current.subtree_size += 1
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
            current.subtree_size += 1
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current

    def __delitem__(self, key: K) -> None:
        self.root = self.delete_aux(self.root, key)

    def delete_aux(self, current: TreeNode, key: K) -> TreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete.
        """

        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left = self.delete_aux(current.left, key)
            current.subtree_size -= 1
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
            current.subtree_size -= 1
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left
            current.subtree_size -= 1

            # general case => find a successor
            succ = self.get_successor(current)
            current.key = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        return current

    def get_successor(self, current: TreeNode) -> TreeNode:
        """
        Get successor of the current node.
        It should be a child node having the smallest key among all the larger keys.
        Best Case: O(Log n) where the tree is balanced and n is the number of nodes of the tree but if the tree has no successor the best case will be O(1).
	    Worst Case : O(N) When the tree is unbalanced where n is number of nodes so it has to trasverse in linear.
    	"""

        if current.right is None:
            return
        else:
            current = current.right
            succesor = self.get_minimal(current)
        return succesor

    def get_minimal(self, current: TreeNode) -> TreeNode:
        """
        Get a node having the smallest key in the current sub-tree.
        Best Case: O(Log n) Where n is number of nodes and happen when the tree is balance but if the tree have no left child and balance then the best case will be O(1).
	    Worst Case : O(N) where n is number of nodes happen when the tree is unbalanced to the left so it must trasverse in linear.
        """
        while current.left is not None:
            current = current.left
        return current

    def is_leaf(self, current: TreeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """

        return current.left is None and current.right is None

    def draw(self, to=sys.stdout):
        """ Draw the tree in the terminal. """

        # get the nodes of the graph to draw recursively
        self.draw_aux(self.root, prefix='', final='', to=to)

    def draw_aux(self, current: TreeNode, prefix='', final='', to=sys.stdout) -> K:
        """ Draw a node and then its children. """

        if current is not None:
            real_prefix = prefix[:-2] + final
            print('{0}{1}'.format(real_prefix, str(current.key)), file=to)

            if current.left or current.right:
                self.draw_aux(current.left, prefix=prefix + '\u2551 ', final='\u255f\u2500', to=to)
                self.draw_aux(current.right, prefix=prefix + '  ', final='\u2559\u2500', to=to)
        else:
            real_prefix = prefix[:-2] + final
            print('{0}'.format(real_prefix), file=to)

    def kth_smallest(self, k: int, current: TreeNode) -> TreeNode:
        """
        Finds the kth smallest value by key in the subtree rooted at current.

        Best Case : O(Log n) where n is the number of nodes and the tree is balanced when k is 1 or size of tree but if it return the root then the best case will be O(1)
	    Worst Case : O(N) where n is the number of nodes when the tree is unbalanced when k is 1 or maximum size of the tree.

        """
        if current.left is not None:
            left_size = current.left.subtree_size
        else:
            left_size = 0

        if k <= left_size and current.left is not None:
            return self.kth_smallest(k, current.left)

        k -= left_size
        if k == 1:
            return current

        if current.right is not None:
            k -= 1
            return self.kth_smallest(k, current.right)

if __name__ == '__main__':
    binary_tree=BinarySearchTree()
    binary_tree[(15, 12, 13)]='b1'
    binary_tree[(25, 22, 23)]='b2'
    binary_tree[(35, 32, 33)]='b3'
    binary_tree[(45, 42, 43)] = 'b4'
    binary_tree[(55, 52, 53)] = 'b5'
    binary_tree.__delitem__(((45, 42, 43)))
    b1=binary_tree[(15, 12, 13)]
    b1='new b1'
    print(binary_tree[(15, 12, 13)])
    print(binary_tree[(45, 42, 43)])
