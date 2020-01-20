import requests
import os

json_header = {'Content-Type': 'application/json'}
zip_header = {'Content-Type': 'application/zip'}
base_url = 'http://s2i-java-atlas-core.apps-dev.hbp.eu'
# base_url = 'http://s2i-java-atlas-core.apps-dev.hbp.eu/' if os.getenv('ATLAS_CORE_ENV') else "http://s2i-java-atlas-core.apps.hbp.eu/"


def get_call(url, without_base_url=False, header=json_header):
    """
    Performs a HTTP-GET call to the Atlas-Core for given url.
    :param url: relative URL to the base URL
    :param without_base_url: if set to TRUE, the given URL can be fully qualified and ignores the Atlas-Core base url
    :param header: Optional request headers. Default header is {'Content-Type': 'application/json'}
    :return: returns the response if status code is OK, otherwise None
    """
    try:
        if without_base_url:
            response = requests.get(url, headers=header)
        else:
            response = requests.get(base_url + url, headers=header)
    except requests.exceptions.RequestException as e:
        print(e)
        response = None
    if response is not None and response.status_code == 200:
        return response
    else:
        return None


def __get_filename_from_header(header):
    name_index = header.index('filename')
    return header[(name_index+9):].replace("\"", "")


def download_tvb_data():
    url = base_url + '/tvb/dummy'
    response = get_call(url, zip_header)
    filename = __get_filename_from_header(response.headers.get('Content-Disposition'))
    with open(filename, 'wb') as code:
        code.write(response.content)
