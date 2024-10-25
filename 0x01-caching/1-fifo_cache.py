#!/usr/bin/env python3
""" Caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Caching system
    using FIFO policy
    """

    def __init__(self):
        """Constructor for class
        """
        self.__key_order = []
        super().__init__()

    def put(self, key, item):
        """Insert cache data
        """
        if key is None or item is None:
            return
        self.__key_order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.__key_order[0]
            self.cache_data.pop(discarded)
            self.__key_order.pop(0)
            print(f"DISCARD: {discarded}")

    def get(self, key):
        """Get cache data
        """
        return self.cache_data.get(key)
