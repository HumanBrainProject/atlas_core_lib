import json

import core
from core.util.client import get_call

base_url = 'http://s2i-java-atlas-core.apps-dev.hbp.eu/'


def get_structure():
    url = base_url + '/allen/structure'
    return json.loads(core.util.client.get_call(url).content.decode('utf-8'))


if __name__ == '__main__':
    print(get_structure())
