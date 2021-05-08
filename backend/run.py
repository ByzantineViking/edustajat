from dotenv import load_dotenv
load_dotenv()  # by default, doesn't override any existing environment variables


import os
from edustajat_service.db.connect import connect
from edustajat_service.refine_data import ehdokkaat, tulokset_ehdokkaittain


# Take HEROKU PORT
port = int(os.environ.get("PORT", 5000))
# Take HEROKU DATABASE_URL
DATABASE_URL = os.environ['DATABASE_URL']


if __name__ == '__main__':
    conn = connect()
    ehdokkaat.run(conn)
    # app.run(debug=True, host='0.0.0.0', port=port)
