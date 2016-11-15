# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)

import sqlite3
from os import path


_cur_dir = path.dirname(path.abspath(__file__))


class DatabaseGateway(object):
    """
    A gateway (http://martinfowler.com/eaaCatalog/gateway.html)
    to a database.
    """

    db_api = sqlite3
    sql_init_scripts = (
        'create_tables.sql',
    )

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = self._init()
        self._cursor = None

    def execute(self, statement, *args):
        with self.connection:
            self.cursor.execute(statement, *args)

    def fetchone(self):
        return self.cursor.fetchone()

    @property
    def cursor(self):
        if self._cursor is None:
            self._cursor = self.connection.cursor()
        return self._cursor

    @classmethod
    def connect(cls, db_name):
        return cls.db_api.connect(db_name)

    def _init(self):
        connection = DatabaseGateway.connect(self.db_name)
        for sql_script in self.sql_init_scripts:
            with open(path.join(_cur_dir, sql_script)) as sql:
                connection.executescript(sql.read())
        return connection
