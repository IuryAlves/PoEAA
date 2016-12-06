# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)

from gateway import DatabaseGateway
from helpers import product_class_factory


class RepositoryStrategy(object):

    def add(self, domain_object):
        raise NotImplementedError

    def remove(self, domain_object):
        raise NotImplementedError

    def find(self, criteria):
        raise NotImplementedError


class DatabaseStrategy(RepositoryStrategy):

    def __init__(self, db_name='database.db'):
        self.gateway = DatabaseGateway(db_name)
        self.gateway.execute('CREATE TABLE IF NOT EXISTS products'
                             '(id INTEGER PRIMARY KEY, name varchar, type varchar)')

    def add(self, domain_object):
        values = domain_object.name, domain_object.type
        self.gateway.execute('INSERT INTO products (name, type)'
                             'VALUES (?, ?)', values)

    def remove(self, name):
        values = (name, )
        self.gateway.execute('DELETE FROM products WHERE name =?', values)

    def find_by_name(self, name):
        values = (name, )
        result = []
        self.gateway.execute('SELECT * FROM products WHERE name like ?', values)
        for row in self.gateway.cursor.fetchall():
            _, name, type_ = row
            Product = product_class_factory()
            result.append(Product(name=name, type=type_))
        return result


class InMemoryStrategy(RepositoryStrategy):

    def __init__(self):
        self.domain_objects = []

    def add(self, domain_object):
        self.domain_objects.append(domain_object)
        return domain_object

    def remove(self, name):
        removed_objects = []
        for domain_object in self.find_by_name(name):
            self.domain_objects.remove(domain_object)
            removed_objects.append(domain_object)
        return removed_objects

    def find_by_name(self, name):
        return list(filter(
            lambda domain_object: domain_object.name == name, self.domain_objects
        ))
