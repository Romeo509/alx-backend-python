#!/usr/bin/env python3
"""
This module contains the safe_first_element function.
"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the list if it exists, otherwise return None.

    Parameters:
    lst (Sequence[Any]): The input list.

    Returns:
    Union[Any, None]: The first element of the
    list if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
