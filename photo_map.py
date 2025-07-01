import os
from typing import List, Dict, Tuple
import piexif
import pyheif
from PIL import Image

SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.heic', '.JPG', '.JPEG', '.HEIC'}


def dms_to_decimal(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1]
    seconds = dms[2][0] / dms[2][1]
    decimal = degrees + minutes / 60 + seconds / 3600
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal


def gps_from_exif(exif_dict) -> Tuple[float, float]:
    gps = exif_dict.get('GPS', {})
    if not gps:
        return None
    lat = gps.get(piexif.GPSIFD.GPSLatitude)
    lat_ref = gps.get(piexif.GPSIFD.GPSLatitudeRef, b'N').decode()
    lon = gps.get(piexif.GPSIFD.GPSLongitude)
    lon_ref = gps.get(piexif.GPSIFD.GPSLongitudeRef, b'E').decode()
    if lat and lon:
        lat_decimal = dms_to_decimal(lat, lat_ref)
        lon_decimal = dms_to_decimal(lon, lon_ref)
        return lat_decimal, lon_decimal
    return None


def extract_exif(path: str):
    ext = os.path.splitext(path)[1].lower()
    if ext in {'.jpg', '.jpeg'}:
        img = Image.open(path)
        exif_bytes = img.info.get('exif')
        if not exif_bytes:
            return None
        exif_dict = piexif.load(exif_bytes)
        return exif_dict
    elif ext == '.heic':
        heif = pyheif.read(path)
        for meta in heif.metadata:
            if meta['type'] == 'Exif':
                return piexif.load(meta['data'])
    return None


def scan_images(folder: str) -> List[Dict]:
    photos = []
    for filename in os.listdir(folder):
        if os.path.splitext(filename)[1] in SUPPORTED_EXTENSIONS:
            path = os.path.join(folder, filename)
            exif = extract_exif(path)
            if not exif:
                continue
            coords = gps_from_exif(exif)
            if not coords:
                continue
            photos.append({'file': path, 'lat': coords[0], 'lon': coords[1]})
    return photos
