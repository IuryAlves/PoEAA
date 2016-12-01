```

>>> from repository import ProductsRepository, InMemoryStrategy
>>> from factories import product_factory
>>> products_repository = ProductsRepository(InMemoryStrategy())
>>> Product = product_factory()
>>> products_repository.add(Product(name='Smart TV', type='Eletronics'))
Product(name='Smart TV', type='Eletronics')

```

```
>>> from repository import ProductsRepository, DatabaseStrategy
>>> products_repository = ProductsRepository(DatabaseStrategy())
>>> Product = product_factory()
>>> products_repository.add(Product(name='Smart TV', type='Eletronics'))
>>> products_repository.find('Smart TV')
[Product(name='Smart TV', type='Eletronics')]

```
