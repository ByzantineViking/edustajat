#!/env/bin/python
import time
from edustajat_service import app


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/municipality', methods=['POST'])
def municipality():
    return 'municipality'


@app.route('/municipalities', methods=['GET'])
def municipalities():
    return 'municipalities'


@app.route('/representative', methods=['POST'])
def representatives():
    return 'representatives'
