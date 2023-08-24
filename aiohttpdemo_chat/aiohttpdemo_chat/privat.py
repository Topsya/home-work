import platform
from datetime import datetime, timedelta
import logging

import aiohttp
import asyncio
from enum import Enum

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
    if platform.system()==  'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print (kod_valyut)
    currency_code = input('Currencie code : ')
    data_need = input('Enter data you need "dd.mm..yyyy": ')
    # new_data=  datetime.now() - datetime.strptime(data_need, "%d.%m.%Y")
    # print (new_data)
    # if new_data <=  timedelta(days=10):
    result = asyncio.run(get_exchange(currency_code, data_need))
    print (result)
    # else :
    #     print ('Your date is more than 10 days ago')

