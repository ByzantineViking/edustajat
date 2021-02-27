#!/env/bin/python
import time
import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
port = int(os.environ.get("PORT", 5000))

app = Flask(__name__,
            # 1. redirect the default static folder path to point to react
            static_folder='../frontend/build',
            # 2. serve without static prefix
            static_url_path='/')




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # remove overhead
app.config['JSON_AS_ASCII'] = False # Add UTF-8 support

db = SQLAlchemy(app)


class Municipality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)

    def __str__(self):
        return f'{self.name}'



class Representative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    municipality_id = db.Column(db.Integer, db.ForeignKey('municipality.id'),
                                nullable=False)
    municipality = db.relationship('Municipality',
                               backref=db.backref('representative', lazy=True))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    #def __repr__(self):
    #    return '<Representative %r>' % f'{self.first_name} {self.last_name}'



@app.route("/")
def index():
    return app.send_static_file('index.html')



@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/municipality', methods=['POST'])
def municipality():
    data = request.json
    municipality = Municipality(
        name=data['name'],
    )
    db.session.add(municipality)
    db.session.commit()
    return f'{municipality}'


@app.route('/municipalities', methods=['GET'])
def municipalities():
    m = Municipality.query.all()
    municipalities = []
    for i in m:
        municipality = {
            "id":i.id,
            "name":i.name
        }
        municipalities.append(municipality)

    print(municipalities
    )
    return jsonify(municipalities)


@app.route('/representative', methods=['POST'])
def representatives():
    data = request.json
    print(data['first_name'])
    representative = Representative(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email']
    )
    db.session.add(representative)
    db.session.commit()
    return f'Added: {representative}'



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)


