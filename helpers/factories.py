# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)


from collections import namedtuple


def product_class_factory():
    return namedtuple('Product', ('name', 'type'))
