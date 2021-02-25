from flask import Flask
from .extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://Karol:1Karol@cluster0.bljx8.mongodb.net/mydb?retryWrites=true&w=majority'

    # connecting mongo with app
    mongo.init_app(app)

    return app

