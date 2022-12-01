import asyncio
from collections import defaultdict

from handlers import *

users = dict()


class Server(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        # self.peername = transport.get_extra_info('peername')
        # print('Connection from {}'.format(self.peername))

    def data_received(self, data):
        message = data.decode()
        try:
            handle(self.transport, message, users)
        except Exception as e:
            self.transport.write((str(e) + '\n').encode(encoding='utf-8'))


async def main():
    loop = asyncio.get_running_loop()
    server = await loop.create_server(Server, '127.0.0.1', 8000)
    await server.serve_forever()


asyncio.run(main())
