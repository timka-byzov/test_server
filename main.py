import asyncio


class Server(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print("DEBUG")
        # self.peername = transport.get_extra_info('peername')
        # print('Connection from {}'.format(self.peername))

    def data_received(self, data):
        message = data.decode()
        print(message)
        self.transport.write(b"DEBUG")


async def main():
    loop = asyncio.get_running_loop()
    server = await loop.create_server(Server, '127.0.0.1', 8000)
    await server.serve_forever()


asyncio.run(main())
