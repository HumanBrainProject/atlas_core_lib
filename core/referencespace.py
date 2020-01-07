import json

import core
from core.util.client import get_call
from core.parcellation import Parcellation


class Referencespace:
    _json_data = None
    name = None

    def __init__(self, json_data):
        self._json_data = json_data
        self.name = json_data['referencespace']['name']

    def __str__(self):
        return "(name: {0})".format(self.name)

    def __repr__(self):
        return self.__str__()

    def get_parcellations(self):
        url = self._json_data['_links']['parcellations']['href']
        result = core.util.client.get_call(url, without_base_url=True)
        parcellations = []
        if result is not None:
            for p in json.loads(result.content.decode('utf-8'))['_embedded']['parcellations']:
                parcellations.append(Parcellation(p['parcellation']['name'], p['_links']))
            return parcellations
        else:
            return None
