from flask import make_response, send_file, request, render_template

from geo_storer.settings.constants import DATA_PATH, GEOJSON, REQUEST_VALUE_NAME
from geo_storer.utils.data_manage import FileManager

from geo_storer import app

@app.route('/download', methods=['GET'])
def download():

    name = request.args.get(REQUEST_VALUE_NAME)
    if name:
        try:
            path = DATA_PATH + name + GEOJSON
            return send_file(path, as_attachment=True)
        except FileNotFoundError:
            return make_response('File not found', 400)
    else:
        return make_response('Wrong value name', 400)


@app.route('/', methods=['GET'])
def index():
    file_manager = FileManager()
    files = zip(file_manager.f_full_names,
                file_manager.f_names)

    return render_template('index.html',
                           files=files)
