import os
import socket

DATA_PATH = os.path.abspath('geodata') + os.path.sep
GEOJSON = '.geojson'
REQUEST_VALUE_NAME = 'name'
PORT = 8000
LOCAL_IP = socket.gethostbyname(socket.gethostname())
