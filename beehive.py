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
        """
        Initialises a BeeHive object
        Args:
        - x: The x coordinate
        - y: The y coordinate
        - z: The z coordinate
        - capacity
        - nutrient_factor
        - volume: default being 0

        Raises: None

        Returns: None, only initializing the item

        Complexity:
        - Worst case: O(1). Only initializing the item.
        - Best case: O(1). Only initializing the item.
        """
        self.x=x
        self.y=y
        self.z=z
        self.capacity=capacity
        self.nutrient_factor=nutrient_factor
        self.volume=volume
        self.emeralds_per_day=min(self.capacity,self.volume)*self.nutrient_factor #how many emeralds per day which is volume_harvested*nutrient_factor

    def __lt__(self, other):
        """
        Compare the emeralds per day of BeeHive
        Args: other. Which is another BeeHive.

        Raises: None

        Returns: A boolean. Of whether self.emeralds_per_day < other.emeralds_per_day

        Complexity:
        - Worst case: O(1). Only comparing variables.
        - Best case: O(1). Only comparing variables.
        """
        return self.emeralds_per_day < other.emeralds_per_day

    def __eq__(self, other):
        """
        Compare the emeralds per day of BeeHive
        Args: other. Which is another BeeHive.

        Raises: None

        Returns: A boolean. Of whether self.emeralds_per_day=other.emeralds_per_day

        Complexity:
        - Worst case: O(1). Only comparing variables.
        - Best case: O(1). Only comparing variables.
        """
        return self.emeralds_per_day == other.emeralds_per_day

    def __le__(self, other):
        """
        Compare the emeralds per day of BeeHive
        Args: other. Which is another BeeHive.

        Raises: None

        Returns: A boolean. Of whether self.emeralds_per_day<=other.emeralds_per_day

        Complexity:
        - Worst case: O(1). When __lt__ is false, so need to call __eq__.
        - Best case: O(1). When __lt__ is false, so no need to call __eq__.
        """
        return self.__lt__(other) or self.__eq__(other)

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        """
        Initialises a BeehiveSelector object
        Args:
        - max_beehives: The max amount of beehives

        Raises: None

        Returns: None, only initializing the item

        Complexity:
        - Worst case: O(1). Only initializing the item.
        - Best case: O(1). Only initializing the item.
        """
        self.max
        self.emeralds_per_day_heap=MaxHeap(max_beehives) #a heap of how much emeralds per day can be gained

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
        Replace all the BeeHives with the list of BeeHives we just put.
        Args:
        - hive_list: A list containing BeeHives.

        Raises: None

        Returns: None

        Complexity:
        - Worst case: O(N). When there are a lot of BeeHive in hive_list.
        - Best case: O(1). When there is only 1 BeeHive in hive_list.
        """
        self.emeralds_per_day_heap = MaxHeap(len(hive_list)) #create a new empty heap
        for hive in hive_list:
            self.emeralds_per_day_heap.add(hive)
    
    def add_beehive(self, hive: Beehive):
        """
        Adds a BeeHive to BeehiveSelector.
        Args:
        - hive: Which is a BeeHive we want to add.

        Raises: None

        Returns: None

        Complexity:
        - Worst case: O(MaxHeap.add). Worst and best the same. Only adding one element.
        - Best case: O(MaxHeap.add)
        """
        self.emeralds_per_day_heap.add(hive)
    
    def harvest_best_beehive(self)-> float:
        """
        Harvest the BeeHive that gives the most emeralds.
        Args: None

        Raises: None

        Returns: How many emeralds we got which is a float

        Complexity:
        - Worst case: O(MaxHeap.get_max+MaxHeap.add). When we harvest the BeeHive and the BeeHive still has volume.
        - Best case: O(MaxHeap.get_max). When we harvest the BeeHive making the BeeHive volume 0. Because the volume is 0we don't add it to our heap.
        """
        harvested_hive=self.emeralds_per_day_heap.get_max() #getting the best hive which is the hive with the most emeralds_per_day
        harvested_volume = min(harvested_hive.capacity, harvested_hive.volume)
        new_volume = harvested_hive.volume - harvested_volume
        if new_volume>0:
            updated_hive = Beehive(harvested_hive.x, harvested_hive.y, harvested_hive.z, harvested_hive.capacity,harvested_hive.nutrient_factor, new_volume)
            self.emeralds_per_day_heap.add(updated_hive) #adding the updated hive with reduced volume
        return harvested_hive.emeralds_per_day

