#!/usr/bin/env python3
"""
This module contains the sum_mixed_list function.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and float numbers.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
