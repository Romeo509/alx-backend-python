#!/usr/bin/env python3
"""
This module contains the safely_get_value function.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:

    """
    Get the value associated with the specified key from the dictionary safely.

    Parameters:
    dct (Mapping): The dictionary from which to retrieve the value.
    key (Any): The key whose associated value is to be retrieved.
    default (Union[T, None], optional): The default value
    to return if the key is not found. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key if
    found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
