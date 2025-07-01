import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from photo_map import dms_to_decimal, scan_images
import os

sample_photo = os.path.join('static', 'photos', 'IMG_3878.HEIC')


def test_dms_to_decimal():
    dms = ((44,1),(8,1),(30,1))
    assert round(dms_to_decimal(dms, 'N'), 6) == 44.141667


def test_scan_images_extracts_coords():
    photos = scan_images(os.path.join('static','photos'))
    assert any(p['file'].endswith('IMG_3878.HEIC') for p in photos)
    coords = [p for p in photos if p['file'].endswith('IMG_3878.HEIC')][0]
    assert 'lat' in coords and 'lon' in coords
