#!/usr/bin/env python3
"""This is a module with type-annotated function"""
from typing import List


def sum_list(input_list: List[float] = []) -> float:
   """This returns list sum as a float"""
    return sum(input_list)
