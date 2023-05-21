from dataclasses import dataclass
from heap import MaxHeap

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
        self.emeralds_per_day=min(self.capacity,self.volume)*self.nutrient_factor #how many emeralds per day which is volume_harvested*nutrient_factor

    def __lt__(self, other):
        return self.emeralds_per_day < other.emeralds_per_day

    def __eq__(self, other):
        return self.emeralds_per_day == other.emeralds_per_day

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.emeralds_per_day_heap=MaxHeap(max_beehives) #a heap of how much emeralds per day can be gained

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.emeralds_per_day_heap = MaxHeap(len(hive_list))
        for hive in hive_list:
            self.emeralds_per_day_heap.add(hive)
    
    def add_beehive(self, hive: Beehive):
        self.emeralds_per_day_heap.add(hive)
    
    def harvest_best_beehive(self)-> float:
        harvested_hive=self.emeralds_per_day_heap.get_max() #getting the best hive which is the hive with the most emeralds_per_day
        harvested_volume = min(harvested_hive.capacity, harvested_hive.volume)
        new_volume = harvested_hive.volume - harvested_volume
        updated_hive = Beehive(harvested_hive.x, harvested_hive.y, harvested_hive.z, harvested_hive.capacity,harvested_hive.nutrient_factor, new_volume)
        self.emeralds_per_day_heap.add(updated_hive) #adding the updated hive with reduced volume
        return harvested_hive.emeralds_per_day

