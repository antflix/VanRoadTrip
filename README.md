# Photo Map Flask App

This app scans images in `static/photos` for GPS data and shows them on an Apple Map using MapKit JS.

## Setup

1. Install dependencies:
   ```bash
   pip install Flask pyheif piexif Pillow
   ```
2. Place your `*.jpg` or `*.heic` images with GPS data into `static/photos`.
3. Generate a MapKit JS token from your Apple developer account and set it in the browser local storage under `MAPKIT_JWT` or replace the placeholder in `templates/index.html`.
4. Run the server:
   ```bash
   python app.py
   ```
5. Navigate to `http://localhost:5000`.

## Running tests

```
pytest
```
