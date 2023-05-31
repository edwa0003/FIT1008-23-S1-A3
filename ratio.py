from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.tree = BinarySearchTree()

    def add_point(self, item: T):
        """
        Attempts to insert an item into the tree.
        Args:
        - item. it uses the item as the key and the item as the value.

        Raises: None

        Returns: None

        Complexity:
        - Worst case: O(BinarySearchTree.__setitem__)=O(logN). N being the amount of elements in the tree.
        This happens when we have to go deep.
        - Best case: O(BinarySearchTree.__setitem__)=O(1). N being the amount of elements in the tree.
        Adding to root.
        """
        self.tree[item] = item

    def remove_point(self, item: T):
        """
        Attempts to delete an item in the tree.
        Args:
        - item. it uses the item as the key.

        Raises: None

        Returns: None

        Complexity:
        - Worst case: O(BinarySearchTree.__delitem__)=O(logN). N being the amount of elements.
        When we are deleting a node that is deep and with two childs.
        - Best case: O(BinarySearchTree.__delitem__)=O(logN). N being the amount of elements.
        When we are deleting a leaf node.
        """
        if self.tree is not None:
            del self.tree[item]

    def ratio(self, x, y):
        """
        Attempts to delete an item in the tree.
        Args:
        - x. Larger than at least x% of the elements in the list
        - y. Smaller than at least y% of the elements in the list

        Raises: None

        Returns: the function in_order_iterative

        Complexity:
        - Worst case: O(kth_smallest+kth_smallest+in_order_iterative)=O(2*logN+logN+O)=O(logN+O). N being the amount of elements in the tree.
        This happens when we need to add a lot of elements.
        - Best case: O(kth_smallest+kth_smallest+in_order_iterative)=O(2*logN+logN+O)=O(logN+O). N being the amount of elements in the tree.
        This happens when only add a few elements.
        """
        min_ratio = ceil(x * len(self.tree) / 100)
        max_ratio = ceil(y * len(self.tree) / 100)

        min_elem = self.tree.kth_smallest(min_ratio + 1, self.tree.root)
        max_elem = self.tree.kth_smallest(len(self.tree) - max_ratio, self.tree.root)

        return self.in_order_iterative(self.tree.root, min_elem, max_elem)

    def in_order_iterative(self, current_node, min_element, max_element):
        """
        Attempts to delete an item in the tree.
        Args:
        - current_node. The node we are currently in.
        - min_element. The lower bound.
        - max_element. The upper bound.

        Raises: None

        Returns: res. Which is a list containing the items we looked for.

        Complexity:
        - Worst case: O(logN+list.append)=O(logN+O). N being the amount of elements in the tree.
        This happens when we need to add a lot of elements.
        - Best case: O(logN+list.append)=O(logN+O). N being the amount of elements in the tree.
        This happens when only add a few elements.
        """
        res = []
        if current_node is None:
            return res

        if current_node.key > max_element.key:
            res += self.in_order_iterative(current_node.left, min_element, max_element)
        elif current_node.key < min_element.key:
            res += self.in_order_iterative(current_node.right, min_element, max_element)
        else:
            res.append(current_node.item)
            res += self.in_order_iterative(current_node.left, min_element, max_element)
            res += self.in_order_iterative(current_node.right, min_element, max_element)
        return res

if __name__ == "__main__":
    points = [4,9,14,15,16,82,87,91,92,99]
    percentiles=Percentiles()
    for point in points:
        percentiles.add_point(point)
    percentiles.ratio(13,10)
    for i in range(2,9):
        print(points[i])


