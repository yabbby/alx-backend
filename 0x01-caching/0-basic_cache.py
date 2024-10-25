#!/usr/bin/env python3
""" Caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching Bluepring
    Parent:
        BaseCaching
    """

    def put(self, key, item):
        """Insert cache data
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get Cache data
        """
        return self.cache_data.get(key)
