from geo_storer import app
from waitress import serve
from geo_storer.utils.address_resolve import AddressResolver

if __name__ == '__main__':
    while True:
        try:
            ip = AddressResolver.get_ip()
            port = AddressResolver.get_port()
            print(f'Server is running on {ip}:{port}')
            serve(app, host=f'{ip}', port=port, url_scheme='https')
            break
        except ValueError:
            print("Wrong host / port specified")
