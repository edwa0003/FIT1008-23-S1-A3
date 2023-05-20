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
    q1: BeeNode | None = None
    q2: BeeNode | None = None
    q3: BeeNode | None = None
    q4: BeeNode | None = None
    q5: BeeNode | None = None
    q6: BeeNode | None = None
    q7: BeeNode | None = None
    q8: BeeNode | None = None

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        if point[0] >= self.key[0]:
            if point[1] >= self.key[1]:
                if point[2] >= self.key[2]:
                    return self.q1
                else:  # z < self.key[2]
                    return self.q5
            else:  # y < self.key[1]
                if point[2] >= self.key[2]:
                    return self.q4
                else:  # z < self.key[2]
                    return self.q8
        else:  # x < self.key[0]
            if point[1] >= self.key[1]:
                if point[2] >= self.key[2]:
                    return self.q2
                else:  # z < self.key[2]
                    return self.q6
            else:  # y < self.key[1]
                if point[2] >= self.key[2]:
                    return self.q3
                else:  # key[2] < current.key[2]
                    return self.q7

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
        return self.get_tree_node_by_key_aux(self.root,key)

    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        if current == None:
            raise KeyError("Key not found: {0}".format(key))
        elif key == current.key:
            return current
        else:
            if key[0] >= current.key[0]:
                if key[1] >= current.key[1]:
                    if key[2] >= current.key[2]:
                        return self.get_tree_node_by_key_aux(current.q1, key)
                    else:  # z < self.key[2]
                        return self.get_tree_node_by_key_aux(current.q5, key)
                else:  # y < self.key[1]
                    if key[2] >= current.key[2]:
                        return self.get_tree_node_by_key_aux(current.q4, key)
                    else:  # z < self.key[2]
                        return self.get_tree_node_by_key_aux(current.q8, key)
            else:  # x < self.key[0]
                if key[1] >= current.key[1]:
                    if key[2] >= current.key[2]:
                        return self.get_tree_node_by_key_aux(current.q2, key)
                    else:  # z < self.key[2]
                        return self.get_tree_node_by_key_aux(current.q6, key)
                else:  # y < self.key[1]
                    if key[2] >= current.key[2]:
                        return self.get_tree_node_by_key_aux(current.q3, key)
                    else:  # key[2] < current.key[2]
                        return self.get_tree_node_by_key_aux(current.q7, key)

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item)
            self.length += 1
            return current
        else:
            if key[0] >= current.key[0]:
                if key[1] >= current.key[1]:
                    if key[2] >= current.key[2]:
                        current.q1 = self.insert_aux(current.q1, key, item)
                        current.subtree_size += 1
                    else:  # z < self.key[2]
                        current.q5 = self.insert_aux(current.q5, key, item)
                        current.subtree_size += 1
                else:  # y < self.key[1]
                    if key[2] >= current.key[2]:
                        current.q4=self.insert_aux(current.q4, key, item)
                        current.subtree_size += 1
                    else:  # z < self.key[2]
                        current.q8 = self.insert_aux(current.q8, key, item)
                        current.subtree_size += 1
            else:  # x < self.key[0]
                if key[1] >= current.key[1]:
                    if key[2] >= current.key[2]:
                        current.q2=self.insert_aux(current.q2, key, item)
                        current.subtree_size += 1
                    else:  # z < self.key[2]
                        current.q6=self.insert_aux(current.q6,key,item)
                        current.subtree_size += 1
                else:  # y < self.key[1]
                    if key[2] >= current.key[2]:
                        current.q3 = self.insert_aux(current.q3, key, item)
                        current.subtree_size += 1
                    else:  # key[2] < current.key[2]
                        current.q7=self.insert_aux(current.q7, key, item)
                        current.subtree_size += 1
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        return current.q1 is None and current.q2 is None and current.q3 is None and current.q4 is None and current.q4 is None and current.q5 is None and current.q6 is None and current.q7 is None and current.q8 is None

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B" #x small, y big, z small
    tdbt[(4, 3, 1)] = "C" #x big, y big, z small
    tdbt[(5, 4, 0)] = "D" #x big, y big, z small, x big, y big, z small
    print('tdbt.root',tdbt.root)
    print('tdbt.root.q6',tdbt.root.q6)
    print('tdbt.root.q5', tdbt.root.q5)
    print('tdbt.root.q5', tdbt.root.q5.q5)
    print(tdbt.root.get_child_for_key((4, 3, 1)))
    #print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
    #        A
    #   /    |
    # B(Q6)  C (Q5)
    #        |
    #        D (Q5)