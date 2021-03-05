#!/env/bin/python
import time
import os

from flask import Flask, render_template, request, jsonify

# Take HEROKU PORT
port = int(os.environ.get("PORT", 5000))
# Take HEROKU DATABASE_URL
DATABASE_URL = os.environ['DATABASE_URL']





app = Flask(__name__,
            # 1. redirect the default static folder path to point to react
            static_folder='../frontend/build',
            # 2. serve without static prefix
            static_url_path='/')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['JSON_AS_ASCII'] = False # Add UTF-8 support




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



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)


