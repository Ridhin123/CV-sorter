from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/file-upload', methods=['POST'])
def file_upload():
    # Handle file upload
    return 'File uploaded'

@app.route('/file-upload', methods=['GET'])
def file_upload_form():
    # Render file upload form
    return render_template('templates/index.html')


if __name__ == "__main__":
    app.run()