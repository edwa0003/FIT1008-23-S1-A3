from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
    Arrange the Points from my_coordinate_list so that when inserted into 3DBeeTree, the 3DBeeTree will be balanced.
    Args:
    - my_coordinate_list: A list of Points to be arranged

    Return:
    - A list of arranged Points to be inserted into 3DBeeTree in its sequence.

    Complexity: See make_ordering_aux
    """
    order = []
    make_ordering_aux(my_coordinate_list,order)
    return order

def make_ordering_aux(my_coordinate_list: list[Point], array: list[Point]) -> list[Point]:
    """
    This function is an auxilary function to make_ordering.
    Its purpose is to find a root given the Points in my_coordinate_list to ensure a balance 3DBeeTree.
    It also calls the property() function to categorize the child Nodes of this root.

    Args:
    - my_coordinate_list: A list of the remaining Points that are not in the sequence yet
    - array: A list of Points in the sequence where they should be inserted into 3DBeeTree (Before adding root)

    Return:
    - A list containing Points in the sequence where they should be inserted into 3DBeeTree (After adding root)

    Complexity:
    - Worst case = O(N logN). N being len(my_coordinate_list). Recursion needed *refer property()*. The tentative depth of the 3DBeeTree.
    - Best case = O(N). N being len(my_coordinate_list). my_coordinate_list has less than 17 elements. No need for recursion.
    """
    if len(my_coordinate_list) <= 17:
        array.extend(my_coordinate_list)

    else:
        x_sorted = Percentiles()
        y_sorted = Percentiles()
        z_sorted = Percentiles()

        for point in my_coordinate_list:
            x_sorted.add_point(point, point[0])
            y_sorted.add_point(point, point[1])
            z_sorted.add_point(point, point[2])

        a = 12.5

        x_ratio = x_sorted.ratio(a,a)
        y_ratio = y_sorted.ratio(a,a)
        z_ratio = z_sorted.ratio(a,a)

        root = None

        for item in my_coordinate_list:
            if item in x_ratio and item in y_ratio and item in z_ratio:
                array.append(item)
                root = item
                my_coordinate_list.remove(item)
                break
            else:
                continue

        properties(my_coordinate_list, root,array)

    return

def properties(my_coordinate_list:list[Point], root:Point , array:list[Point]) -> None:
    """
    This function separates the child Nodes of the current root into 8 categories (octanes), and
    does recursion to repeat the same steps for those octanes.
    Args:
    - my_coordinate_list : A list of points remaining to split into categories after the root is chosen
    - root: The root chosen in make_ordering_aux
    - arr: The sequence of Points to be inserted into 3DBeeTree

    Return: None

    Complexity:
    - Worst = O(n), N being len(my_coordinate_list)
    - Best = O(N), N being len(my_coordinate_list)
    """
    nnn, nnp, npn, npp, pnn, pnp, ppn, ppp = [],[],[],[],[],[],[],[]

    for point in my_coordinate_list:
        if point[0] < root[0] and point[1] < root[1] and point[2] < root[2]:
            nnn.append(point)
        elif point[0] < root[0] and point[1] < root[1] and point[2] >= root[2]:
            nnp.append(point)
        elif point[0] < root[0] and point[1] >= root[1] and point[2] < root[2]:
            npn.append(point)
        elif point[0] < root[0] and point[1] >= root[1] and point[2] >= root[2]:
            npp.append(point)
        elif point[0] >= root[0] and point[1] < root[1] and point[2] < root[2]:
            pnn.append(point)
        elif point[0] >= root[0] and point[1] < root[1] and point[2] >= root[2]:
            pnp.append(point)
        elif point[0] >= root[0] and point[1] >= root[1] and point[2] < root[2]:
            ppn.append(point)
        elif point[0] >= root[0] and point[1] >= root[1] and point[2] >= root[2]:
            ppp.append(point)

    property = [nnn, nnp, npn, npp, pnn, pnp, ppn, ppp]

    for i in range(0,8):
        make_ordering_aux(property[i],array)