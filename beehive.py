from dataclasses import dataclass
from heap import MaxHeap
from threedeebeetree import ThreeDeeBeeTree

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def __lt__(self, other):
        return min(self.capacity, self.volume) * self.nutrient_factor < min(other.capacity, other.volume) * other.nutrient_factor

    def __eq__(self, other):
        return min(self.capacity, self.volume) * self.nutrient_factor == min(other.capacity,other.volume) * other.nutrient_factor

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.emerald_per_day_heap=MaxHeap(max_beehives) #a heap of how much emeralds per day can be gained
        self.hive_tree=ThreeDeeBeeTree()

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.hive_tree = ThreeDeeBeeTree()
        for hive in hive_list:
            self.emerald_per_day_heap.add(hive)
            self.hive_tree[(hive.x,hive.y,hive.z)]=hive
    
    def add_beehive(self, hive: Beehive):
        self.emerald_per_day_heap.add(hive)
        self.hive_tree[(hive.x, hive.y, hive.z)] = hive
    
    def harvest_best_beehive(self)-> float:
        harvested_hive=self.emerald_per_day_heap.get_max()
        return harvested_hive

if __name__ == '__main__':
    b1=Beehive(15, 12, 13, capacity=40, nutrient_factor=5, volume=15) #emerald per day 75
    b2=Beehive(25, 22, 23, capacity=15, nutrient_factor=8, volume=40) #emerald per day 120
    b3=Beehive(35, 32, 33, capacity=40, nutrient_factor=3, volume=40) #emerald per day 120
    b4=Beehive(45, 42, 43, capacity=1, nutrient_factor=85, volume=10) #emerald per day 85
    b5=Beehive(55, 52, 53, capacity=400, nutrient_factor=5000, volume=0)  #emerald per day 0
    beehive_selector=BeehiveSelector(5)
    beehive_selector.set_all_beehives([b1,b2,b3,b4,b5])
    print(beehive_selector.harvest_best_beehive())
    print(b2<=b3)