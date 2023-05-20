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
        self.hive_tree = BinarySearchTree()
        for hive in hive_list:
            emerald_per_day = min(hive.capacity, hive.volume) * hive.nutrient_factor
            self.hive_tree[emerald_per_day]=hive
    
    def add_beehive(self, hive: Beehive):
        emerald_per_day = min(hive.capacity, hive.volume) * hive.nutrient_factor #the amount of emeralds you can gain is volume_harvested*nutrient_factor
        self.emerald_per_day_heap.add(emerald_per_day)
        self.hive_tree[emerald_per_day] = hive
    
    def harvest_best_beehive(self)-> float:
        emeralds_gained=self.emerald_per_day_heap.get_max()
        harvested_hive=self.hive_tree[emeralds_gained]
        volume_harvested=emeralds_gained/harvested_hive.volume
        hive_after_harvest=Beehive(harvested_hive.capacity,harvested_hive.nutrient_factor,harvested_hive.volume-volume_harvested)
        emerald_per_day = min(hive.capacity, hive.volume) * hive.nutrient_factor


if __name__ == '__main__':
