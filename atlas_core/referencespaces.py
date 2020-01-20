import json

from atlas_core.util import client
from atlas_core import parcellations
from atlas_core.referencespace import Referencespace


def get_all_referencespaces():
    result = []
    get_result = client.get_call('/referencespaces')
    if get_result is not None:
        referencespaces = json.loads(get_result.content.decode('utf-8'))['_embedded']['referencespaces']
        for space in referencespaces:
            space_name = space['referencespace']['name']
            result.append(Referencespace(
                space_name,
                parcellations.get_all_parcellations(space_name)
            ))
    return result


def get_referencespace_by_name(name):
    get_result = client.get_call('/referencespaces/' + name)
    if get_result is not None:
        space_name = json.loads(get_result.content.decode('utf-8'))['referencespace']['name']
        return Referencespace(
            space_name,
            parcellations.get_all_parcellations(space_name)
        )
    return None


if __name__ == '__main__':
    print(get_all_referencespaces())
    print('************************************************')
    print(get_referencespace_by_name('colin'))
