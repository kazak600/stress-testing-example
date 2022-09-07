import logging
from aiohttp import web
from datetime import datetime
from pymongo import MongoClient

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    db = request.app['db'].client.main_db
    db.hits.insert_one({'ts': datetime.now(), 'page': 'index'})
    return web.json_response({'status': 'OK', 'page': 'index'})


@routes.get('/main')
async def index(request):
    db = request.app['db'].client.main_db
    db.hits.insert_one({'ts': datetime.now(), 'page': 'main'})
    return web.json_response({'status': 'OK', 'page': 'main'})


@routes.get('/about')
async def index(request):
    db = request.app['db'].client.main_db
    db.hits.insert_one({'ts': datetime.now(), 'page': 'about'})
    return web.json_response({'status': 'OK', 'page': 'about'})


def main():
    app = web.Application()
    app.add_routes(routes)
    app['db'] = getattr(MongoClient(host='mongodb', port=27017, username='admin', password='admin'), 'main_db')

    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)


if __name__ == '__main__':
    main()
