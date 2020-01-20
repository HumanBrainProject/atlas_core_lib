import json

import atlas_core
from atlas_core.util.client import get_call


def get_structure():
    url = '/allen/structure'
    return json.loads(atlas_core.util.client.get_call(url).content.decode('utf-8'))
