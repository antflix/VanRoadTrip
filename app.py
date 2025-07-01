from flask import Flask, render_template, url_for
import os
from photo_map import scan_images

app = Flask(__name__)

IMAGE_DIR = os.path.join('static', 'photos')

@app.route('/')
def index():
    photos = scan_images(IMAGE_DIR)
    return render_template('index.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
