#!/usr/bin/env python3
""" Simple helper function
"""
from typing import List, Dict
import csv
import math


index_range = __import__('0-simple_helper_function').index_range


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
        """Gets page
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)
        result = []
        if start >= len(self.dataset()):
            return result
        result = self.dataset()
        return result[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, str]:
        """Gets an object
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        return {'page_size': page_size,
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': round(len(self.dataset()) / page_size)
                }
