# Gateway Pattern

1. [Introduction](#introduction)
2. [How it works](#how_it_works)
3. [When to use it](#when_to_use_it)
4. [Example](#example)

## Introduction <a name='introduction'></a>

Interesting software rarely lives in isolation. Even the purest object-oriented system often has to deal with things that aren't objects, such as relational data-base tables, CICS transactions, and XML data structures.

When accessing external resources like this, you'll usually get APIs for them. However, these APIs are naturally going to be somewhat complicated because they take the nature of the resource into account. Anyone who needs to under-stand a resource needs to understand its API - whether JDBC and SQL for rela-tional databases or W3C or JDOM for XML. Not only does this make the software harder to understand, it also makes it much harder to change should you shift some data from a relational database to an XML message at some point in the future.

The answer is so common that it's hardly worth stating. Wrap all the special API code into a class whose interface looks like a regular object. Other objects access the resource through this Gateway, which translates the simple method calls into the appropriate specialized API.

*- Martin Fowler*


## How it works <a name='how_it_works'></a>

In reality this is a very simple wrapper pattern. Take the external resource.
What does the application need to do with it? Create a simple API for your
usage and use the *Gateway* to translate to the external source.

*- Martin Fowler*


## When to use it <a name='when_to_use_it'></a>

You should consider using *Gateway* whenever you have an awkward interface
to something that feels external. Rather than let the awkwardness spread
through the whole system, use a *Gateway* to contain it. There's hardly
any downside to making the *Gateway*, and the code elsewhere in the system
 becomes much easier to read.

*- Martin Fowler*
 

## Example <a name='example'></a>

```python

>>> from gateway import DatabaseGateway

>>> gateway = DatabaseGateway('test.db')
>>> gateway.execute('insert into products (name, type) values ("Open Word", "word_processor"))
>>> gateway.execute('select * from products limit 1')
>>> print(gateway.fetchone())
(1, 'Open Word', 'word_processor')
```