import json
from typing import Literal, Union

from pwn import context, remote


class Client:
    def __init__(
        self,
        port: int,
        host="socket.cryptohack.org",
        log_level: Union[
            Literal["debug"], Literal["info"], Literal["warning"], Literal["error"]
        ] = "info",
    ):
        """
        Connect to the CryptoHack interactive challenge running at host:port.

        Examples:
        ```python3
        c = Client(13408)
        c = Client(13408, "socket.cryptohack.org")
        c = Client(13409, "localhost")
        ```
        """
        context.log_level = log_level

        self.r = remote(host, port)

    def get_line(self):
        return self.r.recvline()

    def get_json(self):
        """Returns the next line containing JSON data."""
        while True:
            line = self.get_line()
            try:
                return json.loads(line)
            except Exception:
                pass

    def send_line(self, line: Union[str, bytes]):
        if isinstance(line, str):
            line = line.encode()
        self.r.sendline(line)

    def send_json(self, j):
        self.send_line(json.dumps(j))


class RemoteClient(Client):
    def __init__(self, port: int):
        """Connect to the interactive challenge running at the given port on CryptoHack."""

        Client.__init__(self, port)


class LocalClient(Client):
    def __init__(self, port: int):
        """Connect to the interactive challenge running locally at the given port."""

        Client.__init__(self, port, host="localhost")
