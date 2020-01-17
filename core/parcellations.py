import json

from core import regions
from core.parcellation import Parcellation
from core.util import client


def get_all_parcellations(referencespace):
    """
    Returns a list of all parcellations for a given referencespace
    :param referencespace: Name of the referencespace
    :return: List of Parcellations
    """
    result = []
    get_result = client.get_call('/referencespaces/' + referencespace + '/parcellations')
    if get_result is not None:
        parcellations = json.loads(get_result.content.decode('utf-8'))['_embedded']['parcellations']
        for parcellation in parcellations:
            result.append(Parcellation(
                parcellation['parcellation']['name'],
                referencespace,
                regions.get_all_regions(referencespace, parcellation['parcellation']['name'])
            ))
    return result


def get_parcellation_by_name(referencespace, parcellation):
    """
    Returns a single parcellation for a given referencespace
    :param referencespace: Name of the referencespace
    :param parcellation: Name of the searched parcellation
    :return: A single Parcellation or None
    """
    get_result = client.get_call('/referencespaces/' + referencespace + '/parcellations/' + parcellation)
    if get_result is not None:
        parcellation = json.loads(get_result.content.decode('utf-8'))
        return Parcellation(
            parcellation['parcellation']['name'],
            referencespace,
            regions.get_all_regions(referencespace, parcellation['parcellation']['name'])
        )
    return None


if __name__ == '__main__':
    print(get_all_parcellations('colin'))
    print('************************************************')
    print(get_parcellation_by_name('colin', 'JuBrain Cytoarchitectonic Atlas'))
