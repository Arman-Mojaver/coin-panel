from time import sleep

import click
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient


@click.command()
@click.option('-s', '--symbol', type=str, default='bnbusdt', help='symbol')
@click.option('-id', type=int, default=1, help='ID')
@click.option('-l', '--limit', type=float, required=True)
def main(symbol, id, limit):
    def handler(result, limit=limit):
        price = result.get('p')

        diff = None
        if price:
            diff = float(price) >= limit

        message = f"Price: {price}, Limit: {limit}, Target Reached: {diff}"
        print(message)

        sleep(0.5)

    ws_client = WebsocketClient(stream_url='wss://stream.binance.com:9443')
    ws_client.start()

    ws_client.trade(symbol=symbol, id=id, callback=handler)


if __name__ == '__main__':
    main()
