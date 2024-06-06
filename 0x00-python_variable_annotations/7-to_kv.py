#!/usr/bin/env python3
"""
This module contains the to_kv function.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple containing the string k and the square of v.

    Parameters:
    k (str): The string key.
    v (Union[int, float]): The integer or float value.

    Returns:
    Tuple[str, float]: A tuple containing the
    string k and the square of v as a float.
    """
    return (k, v ** 2.0)
