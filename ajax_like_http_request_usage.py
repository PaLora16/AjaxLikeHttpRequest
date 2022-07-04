from ajax_like_http_request import async_request
from typing import Any


def manage_response(r: Any) -> None:
    """Mamage http request response

    Args:
        r (Any): response from async http frequest
    """
    response = r.json()

    # if there no error, response contains data
    if len(response) > 0:

        data_dict = response[0]

        currency_id = data_dict['id']
        name = data_dict['name']
        price_usd = data_dict['price_usd']

        # Tuple with currency info. In production can be saved into message queue,
        # modify DB record etc. Here just print
        currency_info = (f'id : {currency_id}', f'name : {name}',
                         f'price usd : {price_usd}')

        print(currency_info)


# Get info for currency id 80 ...100
for i in range(80, 100):

    # Ticker URL returns  blockchains currency actual info
    url = f'https://api.coinlore.net/api/ticker/?id={i}'

    # You can see main thread is not blocked as script
    # prints this info first and secondly currency info from the callback
    print(f"Requesting currency id {str(i)}")
    async_request('get', url, timeout=20,
                  callback=manage_response)
