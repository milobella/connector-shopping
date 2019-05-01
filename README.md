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
$ pip install --upgrade .
```

## Run

#### Run the database
```bash
$ docker-compose up -d
```

#### Run the project
```bash
$ shoppinglist_launcher
```

## Requests examples

#### Add item(s)
```bash
$ curl -i -X PUT http://localhost:4848/items -d '[{"item": "carotte"}, {"item": "pain"}]'
HTTP/1.1 204 No Content
Connection: keep-alive
Keep-Alive: 5
Content-Type: text/plain; charset=utf-8
```

#### Get all items
```bash
$ curl -i -X GET http://localhost:4848/items
HTTP/1.1 200 OK
Connection: keep-alive
Keep-Alive: 5
Content-Length: 346
Content-Type: application/json

[{"_id": {"$oid": "5cca0253f8427964e257db5e"}, "item": "carotte", "user_id": "default"}, {"_id": {"$oid": "5cca0253f8427964e257db5f"}, "item": "pain", "user_id": "default"}]
```

#### Delete all items
```bash
$ curl -i -X DELETE http://localhost:4848/items
HTTP/1.1 204 No Content
Connection: keep-alive
Keep-Alive: 5
Content-Type: text/plain; charset=utf-8
```

## CHANGELOGS
- [Application changelog](./CHANGELOG.md)
- [Helm chart changelog](./helm/cerebro/CHANGELOG.md)
