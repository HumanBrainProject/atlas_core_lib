import json

import core
from core.util.client import get_call


def get_all_nodes():
    return json.loads(core.util.client.get_call('/brain/dummy/node').content.decode('utf-8'))


def get_node_information(node):
    return json.loads(core.util.client.get_call(f"/brain/dummy/node/{node}").content.decode('utf-8'))


def get_area_for_node(node):
    return json.loads(core.util.client.get_call(f"/brain/dummy/node/{node}/area").content.decode('utf-8'))


def get_average_orientation_for_node(node):
    return json.loads(core.util.client.get_call(f"/brain/dummy/node/{node}/average-orientation").content.decode('utf-8'))


def get_centre_for_node(node):
    return json.loads(core.util.client.get_call(f"/brain/dummy/node/{node}/centre").content.decode('utf-8'))


def get_cortical_for_node(node):
    return json.loads(core.util.client.get_call(f"/brain/dummy/node/{node}/cortical").content.decode('utf-8'))


def get_tract_length_for_node(node):
    return json.loads(core.util.client.get_call(f"/brain/dummy/node/{node}/tract-length").content.decode('utf-8'))


def get_volume_for_node(node):
    return json.loads(core.util.client.get_call(f"/brain/dummy/node/{node}/volume").content.decode('utf-8'))


def get_weights_for_node(node):
    return json.loads(core.util.client.get_call(f"/brain/dummy/node/{node}/weights").content.decode('utf-8'))


if __name__ == '__main__':
    print(get_area_for_node('Right-Putamen'))
    print(get_average_orientation_for_node('Right-Putamen'))
    print(get_centre_for_node('Right-Putamen'))
    print(get_cortical_for_node('Right-Putamen'))
    print(get_tract_length_for_node('Right-Putamen'))
    print(get_volume_for_node('Right-Putamen'))
    print(get_weights_for_node('Right-Putamen'))




