# Repository Pattern

1. [Introduction](#introduction)
2. [How it works](#how_it_works)
3. [When to use it](#when_to_use_it)
4. [Example](#example)

## Introduction <a name='introduction'></a>


## How it works <a name='how_it_works'></a>


## When to use it <a name='when_to_use_it'></a>


## Example <a name='example'></a>


Using repository with a in memory strategy:

```python

>>> from repository import ProductsRepository, InMemoryStrategy
>>> from factories import product_factory
>>> products_repository = ProductsRepository(InMemoryStrategy())
>>> Product = product_factory()
>>> products_repository.add(Product(name='Smart TV', type='Eletronics'))
Product(name='Smart TV', type='Eletronics')

```

Using the same repository with a database strategy:
```python
>>> from repository import ProductsRepository, DatabaseStrategy
>>> products_repository = ProductsRepository(DatabaseStrategy())
>>> Product = product_factory()
>>> products_repository.add(Product(name='Smart TV', type='Eletronics'))
>>> products_repository.find('Smart TV')
[Product(name='Smart TV', type='Eletronics')]

```
