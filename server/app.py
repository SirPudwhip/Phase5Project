from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate 
from flask_restful import Api, Resource
from flask_media import Media
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from models import db
# from flask_bcrypt import bcrypt



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MEDIA_PATH'] = '../server/videos'
app.config['MEDIA_ALLOWED_EXTENSIONS'] = ['jpg', 'mp4']
app.config['MEDIA_DEFAULT_ENDPOINT'] = 'default'
app.config['MEDIA_DEFAULT_URL'] = 'https://ih1.redbubble.net/image.2924701484.4363/flat,750x,075,f-pad,750x1000,f8f8f8.jpg'
app.json.compact = False


migrate = Migrate(app, db)
db.init_app(app)
 
api = Api(app)

class Home(Resource):
    def get(self):
        return jsonify({'message': 'Welcome to my shitty website '})

api.add_resource(Home, '/')

class

class Uploader(Resource): 
    def post(self):
        file = request.files['file']
        upload = Video()
        upload.media_file.save(file)
        db.session.add(upload)
        db.session.commit
        return make_response({'The request went through':'maybe it saved? Who knows'})

api.add_resource(Uploader, '/uploader')


if __name__ == '__main__':
    app.run(port=5000, debug=True)