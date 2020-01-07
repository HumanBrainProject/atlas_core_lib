import json

import core
from core.referencespace import Referencespace
from core.util.client import get_call


def get_all_referencespaces():
    result = []
    get_result = core.util.client.get_call('/referencespaces')
    if get_result is not None:
        spaces = json.loads(get_result.content.decode('utf-8'))['_embedded']['referencespaces']
        for refspace in spaces:
            result.append(Referencespace(refspace))
    return result


def get_referencespace_by_name(name):
    get_result = core.util.client.get_call('/referencespaces/' + name)
    if get_result is not None:
        space = json.loads(get_result.content.decode('utf-8'))
        return Referencespace(space)
    return None


if __name__ == '__main__':
    for r in get_all_referencespaces():
        print(r)
        print(r.get_parcellations())
        print(r.get_parcellations()[0].get_regions())

    print(get_referencespace_by_name('colin'))
    print(get_referencespace_by_name('collin'))
