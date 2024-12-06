#!/usr/bin/env python3
"""Pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """
    return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    return (start_index, start_index + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns the page with the correct offset and limit"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        current_dataset = self.dataset()
        if start >= len(current_dataset) or end >= len(current_dataset):
            return []

        return current_dataset[start:end]
