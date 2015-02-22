from flask import Flask, request
import cv2
import numpy as numpy
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/upload', methods=['POST', 'GET'])
def hello():
    #Handle POST request
    if request.method == 'POST':
        img = request.files['pic']
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
    pass

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
        
if __name__ == '__main__':
    app.debug = True
    app.run()