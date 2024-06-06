#!/usr/bin/env python3
"""
This module contains the element_length function.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.

    Parameters:
    lst (Iterable[Sequence]): The input list of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains a
    sequence element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
