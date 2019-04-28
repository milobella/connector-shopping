# Shopping list (Shopito)

Shopito is a REST web service which permits to manage a shopping list with a mongodb database.

## Prerequisites

- Having access to [gitlab.milobella.com](https://gitlab.milobella.com/milobella)
- Having ``python 3.6`` installed [instructions](https://docs.python.org/3.6/using/unix.html#getting-and-installing-the-latest-version-of-python)
- Having ``pip3`` installed (Starting with Python 3.4, it is included by default with the Python binary installers)
- [optional] Having ``python virtual environment`` [instructions](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Installation
```bash
$ pip install -r requirements.txt
$ pip install .
```

## Run
```bash
$ shoppinglist_launcher
```

## CHANGELOGS
- [Application changelog](./CHANGELOG.md)
- [Helm chart changelog](./helm/cerebro/CHANGELOG.md)
