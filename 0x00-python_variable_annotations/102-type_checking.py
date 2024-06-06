#!/usr/bin/env python3
from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in on each element in the list by repeating it 'factor' times.

    Parameters:
        lst (List[int]): The input list of integers.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        List[int]: A new list containing each element repeated 'factor' times.
    """
    zoomed_in = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
