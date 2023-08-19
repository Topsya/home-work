import logging
import aiohttp
import jinja2
import aiohttp_jinja2
from aiohttp import web
from privat import get_exchange
from faker import Faker


async def init_app():

    app = web.Application()

    app['websockets'] = dict()

    app.on_shutdown.append(shutdown)

    # aiohttp_jinja2.setup(
    #     app, loader=jinja2.PackageLoader('aiohttpdemo_chat', 'templates'))

    app.router.add_get('/', index)

    return app


async def shutdown(app):
    for ws in app['websockets'].values():
        await ws.close()
    app['websockets'].clear()


async def get_app():
    """Used by aiohttp-devtools for local development."""
    import aiohttp_debugtoolbar
    app = await init_app()
    aiohttp_debugtoolbar.setup(app)
    return app


def main():
    logging.basicConfig(level=logging.DEBUG)

    app = init_app()
    web.run_app(app)


log = logging.getLogger(__name__)

 
def get_random_name():
    fake = Faker()
    return fake.name()


async def index(request):
    ws_current = web.WebSocketResponse()
    ws_ready = ws_current.can_prepare(request)
    if not ws_ready.ok:
        return aiohttp_jinja2.render_template('index.html', request, {})

    await ws_current.prepare(request)

    name = get_random_name()
    log.info('%s joined.', name)

    await ws_current.send_json({'action': 'connect', 'name': name})

    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'join', 'name': name})
    request.app['websockets'][name] = ws_current

    while True:
        msg = await ws_current.receive()
        rate = await get_exchange(msg.data)
        if msg.type == aiohttp.WSMsgType.text:
            for ws in request.app['websockets'].values():
                await ws.send_json(
                    {'action': 'sent', 'name': name, 'text': rate})
        else:
            break

    del request.app['websockets'][name]
    log.info('%s disconnected.', name)
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'disconnect', 'name': name})

    return ws_current


if __name__ == '__main__':
    main()