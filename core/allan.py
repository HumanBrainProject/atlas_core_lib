import json

import core
from core.util.client import get_call


def get_structure():
    url = '/allen/structure'
    return json.loads(core.util.client.get_call(url).content.decode('utf-8'))
