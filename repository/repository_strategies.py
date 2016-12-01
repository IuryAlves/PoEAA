# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)


from gateway import DatabaseGateway
from factories import product_factory


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

    def find(self, name):
        values = (name, )
        result = []
        self.gateway.execute('SELECT * FROM products WHERE name like ?', values)
        for row in self.gateway.cursor.fetchall():
            _, name, type_ = row
            Product = product_factory()
            result.append(Product(name=name, type=type_))
        return result


class InMemoryStrategy(RepositoryStrategy):

    def __init__(self):
        self.domain_objects = []

    def add(self, domain_object):
        self.domain_objects.append(domain_object)
        return domain_object

    def remove(self, domain_object):
        self.domain_objects.remove(domain_object)
        return domain_object

    def find(self, domain_object):
        for item in self.domain_objects:
            if item == domain_object:
                return item
        return None
