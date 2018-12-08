#!/usr/bin/env python
# coding: utf8
from bson.json_util import dumps as bson_dumps
import configparser

from sanic import response, Sanic
from sanic.request import Request

from shoppinglist.database import Database

# Initialize the config
_config = configparser.ConfigParser()
_config.read('shoppinglist.ini')

# Initialize the sanic app
_app = Sanic()

_db = Database(_config['mongo']['host'], _config['mongo'].getint('port'), _config['mongo']['database'])


def main():
    # Run the app
    _app.run(
        host=_config['server']['host'],
        port=_config['server'].getint('port')
    )


@_app.route('/')
async def home(request):
    return response.html('<p>Hello world!</p>')


@_app.route('/items', methods=["PUT"])
async def insert_items(request: Request):
    _db.insert_items_by_user(request.json)
    return response.text("", status=204)


@_app.route('/items', methods=["GET"])
async def get_items(request: Request):
    return _build_resp(_db.get_items_by_user())


@_app.route('/items', methods=["DELETE"])
async def delete_items(request: Request):
    _db.delete_items_by_user()
    return response.text("", status=204)


def _build_resp(result):
    return response.json(result, dumps=bson_dumps)


if __name__ == '__main__':
    main()
