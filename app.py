import os

from flask import Flask
from flask_restful import Api

from Resources.menu import MenuList, Coffee
from Resources.purchase import Purchase, AllPurchases
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_uri = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.secret_key = 'basementcrowd'

api = Api(app)


@app.before_first_request
def create_db():
    db.create_all()


api.add_resource(MenuList, '/menu')
api.add_resource(Coffee, '/coffee/<string:name>')
api.add_resource(Purchase, '/purchase')
api.add_resource(AllPurchases, '/allpurchases')

db.init_app(app)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
