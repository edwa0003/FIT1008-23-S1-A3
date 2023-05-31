from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles
from math import floor

def make_ordering(coordinate_list: list[Point]) -> list[Point]:
    """
    Balancing the input list and return a newly ordered position of points that is balanced so it recursively balance the tree
    until less than or equal to 17 which the base case.
    Args:
    - coordinate_list: which is a list containing points to be balanced

    Raises: None

    Returns: res. Which is a list containing the items we looked for.

    Complexity:
	- Worst Case : O(m * (N LOG N) + (LOG N + O) + (N * O + remove)) Where m is number of iter, n is size of the list and O is length of ratio list.
	Happen when length of list is more than 17 so best case = worst case
	- Best Case : O(m * (N LOG N) + (LOG N + O) + (N * O + remove)) Where m is number of iter, n is size of the list and O is length of ratio list.
	The best case can change to O(1) when the length of list is less or equal to 17.
    """
    result = []

    def process_sublist(lst):
        if len(lst) <= 17:
            result.extend(lst)
        else:
            n = len(lst)
            pivot = floor((n + 7) / 8) / n

            percentiles = [Percentiles() for _ in range(3)]

            for point in lst:
                for i in range(3):
                    percentiles[i].add_point(point[i])

            result_indexes = [percentile.ratio(pivot, pivot) for percentile in percentiles]

            for point in coordinate_list:
                if all(point[i] in result_indexes[i] for i in range(3)):
                    result.append(point)
                    lst.remove(point)
                    break

            mid = len(lst) // 2
            process_sublist(lst[:mid])

    process_sublist(coordinate_list)
    return result