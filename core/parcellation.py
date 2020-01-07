import json

import core
from core.region import Region
from core.util.client import get_call


class Parcellation:
    _name = None
    _links = None

    def __init__(self, name, links):
        self._name = name
        self._links = links

    def __str__(self):
        return "(name: {0})".format(self._name)

    def __repr__(self):
        return self.__str__()

    def get_regions(self):
        result = core.util.client.get_call(self._links['regions']['href'], without_base_url=True)
        regions = []
        if result is not None:
            for r in json.loads(result.content.decode('utf-8'))['_embedded']['regions']:
                regions.append(
                    Region(
                        r['region']['name']
                    )
                )
            return regions
        else:
            return None
