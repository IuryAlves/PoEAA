# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)


class ProductsRepository(object):

    def __init__(self, strategy):
        self._repository_strategy = strategy

    @property
    def repository_strategy(self):
        return self._repository_strategy

    @repository_strategy.setter
    def repository_strategy(self, strategy):
        self._repository_strategy = strategy

    def add(self, value):
        return self.repository_strategy.add(value)

    def remove(self, value):
        return self.repository_strategy.remove(value)

    def find(self, value):
        return self.repository_strategy.find(value)
