from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient


def message_handler(message):
    print(message)


ws_client = WebsocketClient(stream_url='wss://stream.binance.com:9443')
ws_client.start()

symbol = 'bnbusdt'
id = 1
callback = message_handler


methods = {
    'agg_trade': ws_client.agg_trade,
    'trade': ws_client.trade,
    'kline': ws_client.kline,
}


methods['agg_trade'](symbol=symbol, id=id, callback=callback)