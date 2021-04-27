import os
from flask import Flask


app = Flask(__name__,
            # 1. redirect the default static folder path to point to react
            static_folder='../frontend/build',
            # 2. serve without static prefix
            static_url_path='/')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['JSON_AS_ASCII'] = False  # Add UTF-8 support


