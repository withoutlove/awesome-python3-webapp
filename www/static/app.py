import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

#路由器装饰
routes=web.RouteTableDef()

@routes.get('/')
async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')
async def my_app():
    app=web.Application()
    app.add_routes(routes)
    return app
web.run_app(my_app(),host='127.0.0.1',port=9000)