#Import flask and template operators
from flask import Flask, render_template

#Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

#Define the WSGI application object
app = Flask(__name__)

#Configurations
app.config.from_object('config')

#Define the database object which is imported
#by modules and controllers
db = SQLAlchemy(app)

#Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

#Import a module / component using its blueprint handler variable
from app.img_upload.controllers import img_upload as img_upload

#Register Blueprints
app.register_blueprint(img_upload)
# app.register_blueprint(module)

#Build the database:
db.create_all()
