from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        raise NotImplementedError()


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0


    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        raise NotImplementedError()

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key,item)
            self.length += 1
        elif key[0] < current.key[0] and key[1]<current.key[1] and key[2]<current.key[2]:

        elif key[0] < current.key[1]

        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        raise NotImplementedError()

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B" #x small, y large, z small
    tdbt[(4, 3, 1)] = "C" #x big, y same, z small
    tdbt[(5, 4, 0)] = "D" #x big, y large,z small
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
    #        A
    #   /    |
    # B(Q6)  C (Q8)
    #        |
    #        D (Q8)