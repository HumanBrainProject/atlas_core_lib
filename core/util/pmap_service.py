import requests

# URL for the pmap-service
url = 'http://pmap-pmap-service.apps-dev.hbp.eu/multimerge'


def retrieve_probability_map(area_name, hemisphere, threshold):
    """
    Retrieves a probability map for an area
    :param area_name: Name of the area
    :param hemisphere: The Hemisphere. Should be provided through the enum
    :param threshold: Threshold or the probability map
    :return: returns the response if status is OK, otherwise None
    """
    try:
        data = '{ "areas": [{"name": "' + area_name + \
               '","hemisphere": "' + hemisphere + '" }], "threshold": ' + str(threshold) + '}'
        response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
    except requests.exceptions.RequestException as e:
        print(e)
        response = None
    if response is not None and response.status_code == 200:
        return response
    else:
        print('response', response)
        return None


if __name__ == '__main__':
    roi = retrieve_probability_map('Area-Fp1', 'left', 0.7)
    print(roi.content)
    print(roi.status_code)
