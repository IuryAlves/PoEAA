# Repository Pattern

1. [Introduction](#introduction)
2. [How it works](#how_it_works)
3. [When to use it](#when_to_use_it)
4. [Example](#example)
5. [Iury's notes](#notes)

## Introduction <a name='introduction'></a>

A *Repository* mediates between the domain and the data mapping layers, acting like an in-memory
domain object collection. 

Objects can be added to and removed from the *Repository*. as they can from a simple collection of 
objects, and the mapping code encapsulated by the *Repository* will carry out the appropiate operations
behind the scenes.

*Repository* supports hte objective of achieving a clean separation and one way dependency between the domain and data mapping layers.

## How it works <a name='how_it_works'></a>

TODO

## When to use it <a name='when_to_use_it'></a>

In a large system with many domain objects types and many possible queries, a *Repository* reduces
the amount of code needed to deal with all querying that goes on.

Situations whith multiple data sources are where we really see the *Repository* coming into its own, for example, that we're sometimes interested in using a simple in-memory data store, commonly when we wants to run a suite of unit tests entirely in memory for better performance [[1]](#1). With no database access, many lenghty tests suites run significantly faster. 


## Example <a name='example'></a>


Using repository with a in memory strategy:

```python

>>> from repository import ProductsRepository, InMemoryStrategy
>>> from helpers import product_class_factory
>>> products_repository = ProductsRepository(InMemoryStrategy())
>>> Product = product_class_factory()
>>> products_repository.add(Product(name='Smart TV', type='Eletronics'))
Product(name='Smart TV', type='Eletronics')
>>> products_repository.find_by_name(name='Smart TV')
[Product(name='Smart TV', type='Eletronics')]
>>> products_repository.remove(name='Smart TV')
[Product(name='Smart TV', type='Eletronics')]

```

Using the same repository with a database strategy:
```python
>>> from repository import ProductsRepository, DatabaseStrategy
>>> from helpers import product_class_factory
>>> products_repository = ProductsRepository(DatabaseStrategy())
>>> Product = product_class_factory()
>>> products_repository.add(Product(name='Smart TV', type='Eletronics'))
>>> products_repository.find_by_name(name='Smart TV')
[Product(name='Smart TV', type='Eletronics')]

```


## Iury's notes <a name='notes'></a>


<a name='1'></a>

In my opinion your unit tests should run against the same database that you uses in production. This makes your application with more [parity](https://12factor.net/dev-prod-parity) and allows you to reproduce bugs that happen in production with more consistency.