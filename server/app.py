from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate 
from flask_restful import Api, Resource
from flask_media import Media
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


# from models import 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MEDIA_PATH'] = '../server/videos'
app.config['MEDIA_ALLOWED_EXTENSIONS'] = ['jpg', 'mp4']
app.config['MEDIA_DEFAULT_ENDPOINT'] = 'default'
app.config['MEDIA_DEFAULT_URL'] = 'https://ih1.redbubble.net/image.2924701484.4363/flat,750x,075,f-pad,750x1000,f8f8f8.jpg'
app.json.compact = False

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return jsonify({'message': 'Hello, World!'})

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)