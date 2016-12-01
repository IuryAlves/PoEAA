# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)


class POPO(object):

    """
    Plain Old Python Object
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        vars_ = ", ".join("%s='%s'" % item for item in vars(self).items()) 
        return '{class_name}({dict})'.format(
            class_name=self.__class__.__name__,
            dict=vars_
        )
