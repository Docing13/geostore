from geo_storer import app
from waitress import serve

from geo_storer.settings.constants import PORT, LOCAL_IP

if __name__ == '__main__':

    print(f'Server is running on {LOCAL_IP}:{PORT}')
    serve(app, host=f'{LOCAL_IP}', port=PORT, url_scheme='https')

