class User:

    def __init__(self, transport, name: str):
        self.transport = transport
        self.name = name.strip()
