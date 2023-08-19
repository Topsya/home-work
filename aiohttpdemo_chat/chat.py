import logging
import aiohttp
import jinja2
import aiohttp_jinja2
from aiohttp import web
# from aiohttpdemo_chat.main import get_exchange
from faker import Faker
import platform
from datetime import datetime, timedelta
import asyncio
from enum import Enum


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


class CurrenciesEnum(Enum):
    USD= 'USD'  # долар США
    EUR= 'EUR'	# евро
    CHF= 'CHF'	# швейцарський франк
    GBP= 'GBP'	# британський фунт
    PLZ= 'PLZ'	# польський злотий
    SEK= 'SEK'	# шведська крона
    XAU= 'XAU'	# золото
    CAD= 'CAD'  # канадський долар

kod_valyut = ' USD	долар США\n EUR	євро\n CHF	швейцарський франк\n GBP	британський фунт\n PLZ	польський злотий\n SEK	шведська крона\n XAU	золото \n CAD	канадський долар '   
async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    r = await resp.json()
                    return r
                logging.error(f"Error status: {resp.status} for {url}")
                return None
        except aiohttp.ClientConnectorError as err:
            logging.error(f"Connection error: {str(err)}")
            return None



async def get_exchange(currency_code: CurrenciesEnum, data_need):
    result = await request(f'https://api.privatbank.ua/p24api/exchange_rates?date={data_need}')
    if result:
        rates = result.get("exchangeRate")
        exc, = list(filter(lambda element: element["currency"] == currency_code, rates))
        return f"On this data {data_need},  {currency_code}: buy: {exc['purchaseRateNB']}, sale: {exc['saleRateNB']}. Date today: {datetime.now().date()}"
    return "Failed to retrieve data"


if __name__ == '__main__':
    main()
    if platform.system()==  'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print (kod_valyut)
    currency_code = input('Currencie code : ')
    data_need = input('Enter data you need "dd.mm..yyyy": ')
    new_data=  datetime.now() - datetime.strptime(data_need, "%d.%m.%Y")
    print (new_data)
    if new_data <=  timedelta(days=10):
        result = asyncio.run(get_exchange(currency_code, data_need))
        print (result)
    else :
        print ('Your date is more than 10 days ago')


# if __name__ == '__main__':
#     main()
