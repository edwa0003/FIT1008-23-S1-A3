from dataclasses import dataclass
from heap import MaxHeap
from referential_array import ArrayR

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
        self.max_beehives=max_beehives
        self.hive_array=ArrayR(self.max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.hive_array = ArrayR(self.max_beehives) #create an empty array
        for i in range(len(hive_list)): #adding the beehive one by one to the array
            self.hive_array[i]=hive_list[i]
    
    def add_beehive(self, hive: Beehive):
        raise NotImplementedError()
    
    def harvest_best_beehive(self):
        raise NotImplementedError()
