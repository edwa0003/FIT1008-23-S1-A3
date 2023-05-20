from dataclasses import dataclass
from heap import MaxHeap
from bst import BinarySearchTree

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.emerald_per_day_heap=MaxHeap(max_beehives) #a heap of how much emeralds per day can be gained
        self.hive_tree=BinarySearchTree()

    def set_all_beehives(self, hive_list: list[Beehive]):
        for hive in hive_list:
            emerald_per_day = min(hive.capacity, hive.volume) * hive.nutrient_factor
            self.hive_tree[emerald_per_day]=hive
    
    def add_beehive(self, hive: Beehive):
        self.emerald_per_day_heap.add(min(hive.capacity,hive.volume)*hive.nutrient_factor) #the amount of emeralds you can gain is volume_harvested*nutrient_factor
    
    def harvest_best_beehive(self)-> float:
        emeralds_gained=self.emerald_per_day_heap.get_max()

if __name__ == '__main__':
    h = MaxHeap(5)
    b1, b2, b3, b4, b5 = (
        Beehive(15, 12, 13, capacity=40, nutrient_factor=5, volume=15),
        Beehive(25, 22, 23, capacity=15, nutrient_factor=8, volume=40),
        Beehive(35, 32, 33, capacity=40, nutrient_factor=3, volume=40),
        Beehive(45, 42, 43, capacity=1, nutrient_factor=85, volume=10),
        Beehive(55, 52, 53, capacity=400, nutrient_factor=5000, volume=0),
    )
    for hive in [b1, b2, b3, b4, b5]:
        h.add(hive)