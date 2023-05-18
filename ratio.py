from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree
from data_structures.mergesort import mergesort

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.points = []
        self.tree = BinarySearchTree()
    
    def add_point(self, item: T):
        self.tree[item] = item
    
    def remove_point(self, item: T):
        del self.tree[item]

    def ratio(self, x, y):
        self.points = self.tree.to_list()
        print(self.points)

        totalElements = len(self.points)
        largerThan = ceil((x / 100) * totalElements)
        smallerThan = totalElements - ceil((y / 100) * totalElements)
        print(largerThan, smallerThan)
        if largerThan <= 0 and smallerThan <= 0:
            return []

        return self.points[largerThan:smallerThan]

if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
