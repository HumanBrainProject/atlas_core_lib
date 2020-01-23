import json

import ebrains_atlascore
from ebrains_atlascore.util.client import get_call


def get_structure():
    url = '/allen/structure'
    return json.loads(ebrains_atlascore.util.client.get_call(url).content.decode('utf-8'))
