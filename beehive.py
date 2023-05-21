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

    def __init__(self,x,y,z,capacity,nutrient_factor,volume=0):
        self.x=x
        self.y=y
        self.z=z
        self.capacity=capacity
        self.nutrient_factor=nutrient_factor
        self.volume=volume
        self.emeralds_per_day=min(self.capacity,self.volume)*self.nutrient_factor

    def __lt__(self, other):
        return self.emeralds_per_day < other.emeralds_per_day

    def __eq__(self, other):
        return self.emeralds_per_day == other.emeralds_per_day

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.emerald_per_day_heap=MaxHeap(max_beehives) #a heap of how much emeralds per day can be gained

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.emerald_per_day_heap = MaxHeap(len(hive_list))
        for hive in hive_list:
            self.emerald_per_day_heap.add(hive)
    
    def add_beehive(self, hive: Beehive):
        self.emerald_per_day_heap.add(hive)
    
    def harvest_best_beehive(self)-> float:
        harvested_hive=self.emerald_per_day_heap.get_max()
        print('harvested hive before volume change: ',harvested_hive)
        harvested_volume=min(harvested_hive.capacity,harvested_hive.volume)
        print('harvested_volume',harvested_volume)
        new_volume=harvested_hive.volume-harvested_volume
        updated_hive=Beehive(harvested_hive.x,harvested_hive.y,harvested_hive.z,harvested_hive.capacity,harvested_hive.nutrient_factor,new_volume)
        self.emerald_per_day_heap.add(updated_hive)
        return harvested_hive.emeralds_per_day

if __name__ == '__main__':
    b1=Beehive(15, 12, 13, capacity=40, nutrient_factor=5, volume=15) #emerald per day 75
    b2=Beehive(25, 22, 23, capacity=15, nutrient_factor=8, volume=40) #emerald per day 120
    b3=Beehive(35, 32, 33, capacity=40, nutrient_factor=3, volume=40) #emerald per day 120
    b4=Beehive(45, 42, 43, capacity=1, nutrient_factor=85, volume=10) #emerald per day 85
    b5=Beehive(55, 52, 53, capacity=400, nutrient_factor=5000, volume=0)  #emerald per day 0
    beehive_selector=BeehiveSelector(5)
    beehive_selector.set_all_beehives([b1,b2,b3,b4,b5])
    print(beehive_selector.harvest_best_beehive())
    print(beehive_selector.harvest_best_beehive())
    print(beehive_selector.harvest_best_beehive())
    print(beehive_selector.harvest_best_beehive())
    print(beehive_selector.harvest_best_beehive())