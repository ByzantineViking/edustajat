import os
from dotenv import load_dotenv
load_dotenv() #  by default, doesn't override any existing environment variables
from edustajat_service.db.connect import connect
from edustajat_service.refine_data.ehdokkaat import refine_ehdokkaat
from edustajat_service import app, port
# Take HEROKU PORT
port = int(os.environ.get("PORT", 5000))
# Take HEROKU DATABASE_URL
DATABASE_URL = os.environ['DATABASE_URL']
print(port)
if __name__ == '__main__':
    # connect()
    refine_ehdokkaat()
    # app.run(debug=True, host='0.0.0.0', port=port)
