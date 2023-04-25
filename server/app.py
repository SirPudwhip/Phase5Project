from flask import Flask, request, make_response
from flask_migrate import Migrate 
from flask_restful import Api, Resource
from flask_media import Media
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


# from models import 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.json.compact = False

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        return make_response({"message":"This is working"})

api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)