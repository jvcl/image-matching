from flask import Flask, request
import cv2
import numpy as numpy
from werkzeug import secure_filename
import os
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy

# configuration
DEBUG = True
SECRET_KEY = 'secret'
USERNAME = 'admin'
PASSWORD = 'password'
# Set root folder and application name
ROOT = os.path.abspath(os.path.dirname(__file__))
# assuming application name is same as folder
APP_NAME = os.path.basename(ROOT)
DATABASE_NAME = "images.db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ROOT, "tmp/" + DATABASE_NAME)

# Set up App
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    origin = db.Column(db.String(50))
    rating = db.Column(db.Float)
    date_added = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('items', lazy='dynamic'))

    def __init__(self, title, origin, category, rating= None, date_added = None):
        self.title = title
        self.origin = origin
        if rating is None:
            rating = 0.0
        self.rating = rating
        self.category = category
        if date_added is None:
            date_added = datetime.utcnow()
        self.date_added = date_added

        def __repr__(self):
            return '<Item %r>' % self.name

@app.route('/upload', methods=['POST', 'GET'])
def hello():
    #Handle POST request
    if request.method == 'POST':
        img = request.files['pic']
        #TODO, SAVE IMAGE TO FOLDER.
        name = secure_filename(img.filename)
        calculate_sift(img, name)
        return "Done"
    #Handle GET request
    elif request.method == 'GET':
        return '''
            <form action="" method="post" enctype="multipart/form-data">
                <input type="file" name="pic" accept="image/*">
                <input type="submit">
            </form>
        '''
    
@app.route('/add-image', methods=['POST', 'GET'])
def add_image():
    """
    Method to add an image to the db
    """
    #Handle POST request
    if request.method == 'POST':
        img = request.files['pic']
        name = secure_filename(img.filename)
        #Method calculate sift descriptors, and returns the descriptor & Keypoint to be saved
        calculate_sift(img, name)
        #TODO, SAVE IMAGE, DESCRIPTORS, KEYPOINTS, ADD ENTRY TO DB
        return "Done"
        #Handle GET request, ONLY FOR TESTING
    #Handle GET request
    elif request.method == 'GET':
        return '''
            <form action="" method="post" enctype="multipart/form-data">
                <input type="file" name="pic" accept="image/*">
                <input type="submit">
            </form>
        '''

@app.route('/get-match', methods=['POST', 'GET'])
def get_match():
    """
    Method to query the application for a match. It recives a photo to be 
    matched against the database
    """
    #Handle POST request
    if request.method == 'POST':
        img = request.files['pic']
        name = secure_filename(img.filename)
        #TODO calculate sift then look for a match in the db

@app.route('/user/<username>/<passs>')
def userName(username, passs):
    return "Hello " + username + " " + passs

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

"""
IMAGE PROCESSING METHODS
"""
def calculate_sift(img, name):
    #Convert image to numpy array
        img = numpy.asarray(bytearray(img.read()), dtype=numpy.uint8)
        #Read image from memory
        img = cv2.imdecode(img, cv2.CV_LOAD_IMAGE_UNCHANGED)
        #Gray scale image
        gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #load sift
        sift = cv2.SIFT()
        #Detect the KeyPoints descriptors
        kp = sift.detect(gray,None)
        
        #Save to file
        img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imwrite(name, img)

        #TODO return the Keypont and descriptor
        
if __name__ == '__main__':
    app.run()