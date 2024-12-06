#!/usr/bin/env python3
"""Pagination"""


def index_range(page: int, page_size: int):
    """
    return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    return (start_index, start_index + page_size)
