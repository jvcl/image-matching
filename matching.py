from flask import Flask, request
import cv2
import numpy as numpy
from werkzeug import secure_filename

# configuration
DATABASE = '/tmp/matching.db'
DEBUG = True
SECRET_KEY = 'secret'
USERNAME = 'admin'
PASSWORD = 'password'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

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