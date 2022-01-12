from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import DpawRegion

dpawregion_mapping = {
    'feat_id': 'id',
    'ogc_fid': 'ogc_fid',
    'region': 'region',
    'office': 'office',
    'hectares': 'hectares',
    'md5_rowhash': 'md5_rowhash',
    'geom': 'MULTIPOLYGON',
}


region_json = Path(__file__).resolve().parent / 'data' / 'json' / 'dpaw_regions.json'

def run(verbose=True):
    lm = LayerMapping(DpawRegion, region_json, dpawregion_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
