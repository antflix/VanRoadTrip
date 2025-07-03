# Photo Map Flask App

This app scans images in `static/photos` for GPS data and shows them on an Apple Map using MapKit JS.

## Setup

1. Install dependencies:
   ```bash
   pip install Flask pyheif piexif Pillow
   ```
2. Place your `*.jpg` or `*.heic` images with GPS data into `static/photos`.
3. Place your `location-history.json` file (exported from Google Maps Timeline) in the project root.
4. Generate a MapKit JS token from your Apple developer account and set it in the browser local storage under `MAPKIT_JWT` or replace the placeholder in `templates/index.html`.
5. Run the server:
   ```bash
   python app.py
   ```
6. Navigate to `http://localhost:5000`.

## Running tests

```
pytest
```
