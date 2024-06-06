#!/usr/bin/env python3
"""
This module contains the make_multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier to use in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float
    argument and returns
    the result of multiplying it by the multiplier.
    """

    def multiplier_func(num: float) -> float:
        """
        Multiply a number by the multiplier.

        Parameters:
        num (float): The number to multiply.

        Returns:
        float: The result of multiplying the number by the multiplier.
        """
        return num * multiplier
    return multiplier_func
