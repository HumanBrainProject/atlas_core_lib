import json

from ebrains_atlascore.util import client
from ebrains_atlascore import parcellations
from ebrains_atlascore.referencespace import Referencespace


def get_all_referencespaces():
    result = []
    get_result = client.get_call('/referencespaces')
    if get_result is not None:
        referencespaces = json.loads(get_result.content.decode('utf-8'))['_embedded']['referencespaces']
        for space in referencespaces:
            space_name = space['referencespace']['name']
            space_id = space['referencespace']['id']
            result.append(Referencespace(
                space_name,
                space_id,
                parcellations.get_all_parcellations(space_name)
            ))
    return result


def get_referencespace_by_id(id):
    get_result = client.get_call('/referencespaces/' + id)
    if get_result is not None:
        space_name = json.loads(get_result.content.decode('utf-8'))['referencespace']['name']
        space_id = json.loads(get_result.content.decode('utf-8'))['referencespace']['id']
        return Referencespace(
            space_name,
            space_id,
            parcellations.get_all_parcellations(space_name)
        )
    return None


if __name__ == '__main__':
    print(get_all_referencespaces())
    print('************************************************')
    print(get_referencespace_by_id('dafcffc5-4826-4bf1-8ff6-46b8a31ff8e2'))
