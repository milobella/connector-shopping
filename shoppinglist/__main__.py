#!/usr/bin/env python
# coding: utf8
from bson.json_util import dumps
from sanic import response, Sanic
from sanic.request import Request

from shoppinglist.configuration import read_config
from shoppinglist.database import Database

# Initialize the config
_config = read_config('shoppinglist.ini')

# Initialize the sanic app
_app = Sanic()

_db = Database(
    _config('host', namespace='mongo'),
    _config('port', namespace='mongo', parser=int),
    _config('database', namespace='mongo'),
)


def main():
    # Run the app
    _app.run(
        host=_config('host', namespace='server'),
        port=_config('port', namespace='server', parser=int),
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
    if 'items' in request.args:
        _db.delete_items_by_user(request.args["items"])
    else:
        _db.empty_list_by_user()
    return response.text("", status=204)


def _build_resp(result):
    return response.json(result, dumps=dumps)


if __name__ == '__main__':
    main()
