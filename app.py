from flask import Flask, render_template, url_for, send_from_directory
import os
from photo_map import scan_images

app = Flask(__name__)

IMAGE_DIR = os.path.join('static', 'photos')

@app.route('/')
def index():
    photos = scan_images(IMAGE_DIR)
    return render_template('index.html', photos=photos)

@app.route('/location-history.json')
def location_history():
    return send_from_directory(app.root_path, 'location-history.json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
