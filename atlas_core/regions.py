import json

from atlas_core.util import client, pmap_service
from atlas_core.region import Region
from atlas_core.util.hemisphere import Hemisphere


def get_all_regions(referencespace, parcellation):
    result = []
    get_result = client.get_call(
        '/referencespaces/' + referencespace + '/parcellations/' + parcellation + '/regions'
    )
    if get_result is not None:
        regions = json.loads(get_result.content.decode('utf-8'))['_embedded']['regions']
        for region in regions:
            result.append(Region(
                region['region']['name'],
                referencespace,
                parcellation,
                kwargs=region['region']
            ))
    return result


def get_region_by_name(referencespace, parcellation, region):
    get_result = client.get_call(
        '/referencespaces/' + referencespace + '/parcellations/' + parcellation + '/regions/' + region
    )
    if get_result is not None:
        region = json.loads(get_result.content.decode('utf-8'))
        return Region(
            region['region']['name'],
            referencespace,
            parcellation,
            kwargs=region['region']
        )
    return None


def get_probability_map_for_region(region_name, hemisphere, threshold):
    return pmap_service.retrieve_probability_map(region_name, hemisphere, threshold)


if __name__ == '__main__':
    print('************************************************')
    print(get_region_by_name('colin', 'JuBrain Cytoarchitectonic Atlas', 'LB (Amygdala) - left hemisphere'))
    print(get_region_by_name('tvb', 'tvb', 'Left-Frontal-pole'))
    print(get_probability_map_for_region('Area-Fp1', Hemisphere.LEFT.value, 0.2))
