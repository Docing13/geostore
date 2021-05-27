import socket

from geo_storer.settings.constants import PORT, LOCAL_IP


class AddressResolver:

    @staticmethod
    def get_ip() -> str:
        """
        Getting valid ip
        :return str:
        """
        while True:
            addr = input(f"IP (default {LOCAL_IP}): ")
            if addr == '':
                return LOCAL_IP
            try:
                socket.inet_aton(addr)
                break
            except socket.error:
                print("Wrong ip")
        return addr

    @staticmethod
    def get_port() -> int:
        """
        Getting valid port
        :return int:
        """
        while True:
            port = input(f"PORT (default {PORT}): ")
            print(port)
            if port == '':
                return PORT
            try:
                port = int(port)
                if port < 1:
                    raise ValueError
                break
            except ValueError:
                print("Wrong port")
        return port
