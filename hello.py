#import flask
import os,sys
import time
from flask import Response, Flask, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import subprocess

UPLOAD_FOLDER = 'upload/'
ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def get():
    with open('test.log', 'w') as f:
        process = subprocess.Popen('python label_image.py upload/test.jpg',shell=True, stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, ''):
            sys.stdout.write(line)
            f.write(line)


    return hello



# def get_data():
#     """
#     Return a string that is the output from subprocess
#     """

   
#     def inner():
#         proc = subprocess.Popen(
#             ['python label_image.py upload/test.jpg'],          
#             shell=True,
#             stdout=subprocess.PIPE
#         )
#         printCount=0
#         for line in iter(proc.stdout.readline,''):
#             time.sleep(1)                          
#             output = line.rstrip() + '<br/>\n'
#             output = request.form
#             printCount=printCount+1
#             if printCount==4:
#                break
               
#     return  



@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'test.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return get()
               
     
if __name__ == '__main__':
    app.debug=True
    app.run(host = '0.0.0.0')

