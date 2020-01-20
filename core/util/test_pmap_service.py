from unittest import TestCase, mock, main
from unittest.mock import Mock

from requests import RequestException

from core.util import pmap_service
from core.util.hemisphere import Hemisphere


def _mock_response(status=200, content="CONTENT"):

    mock_resp = Mock()
    mock_resp.status_code = status
    mock_resp.content = content
    return mock_resp


area_name = "Area-Fp1"
url = 'http://pmap-pmap-service.apps-dev.hbp.eu/multimerge'
hemisphere = Hemisphere.LEFT.value
threshold = 0.2


def create_body():
    return '{ "areas": [{"name": "' + area_name + \
           '","hemisphere": "' + hemisphere + '" }], "threshold": ' + str(threshold) + '}'


class TestPmapService(TestCase):

    valid_result_data = 'RESULT_DATA'

    @mock.patch('request.post')
    def test_valid_response(self, mock_post):
        mock_resp = _mock_response(content=self.valid_result_data)
        mock_post.return_value = mock_resp

        result = pmap_service.retrieve_probability_map(area_name, hemisphere, threshold)
        self.assertEqual(result.content, self.valid_result_data)
        self.assertEqual(result.status_code, 200)
        mock_post.assert_called_with(url, data=create_body(), headers={'Content-Type': 'application/json'})

    @mock.patch('request.post')
    def test_content_not_none_but_wrong_status(self, mock_post):
        mock_resp = _mock_response(content=self.valid_result_data, status=418)
        mock_post.return_value = mock_resp

        result = pmap_service.retrieve_probability_map(area_name, hemisphere, threshold)
        self.assertEqual(result, None)

    @mock.patch('request.post')
    def test_content_none(self, mock_post):
        mock_resp = None
        mock_post.return_value = mock_resp

        result = pmap_service.retrieve_probability_map(area_name, hemisphere, threshold)
        self.assertEqual(result, None)

    @mock.patch('request.post')
    def test_requests_throws_exception(self, mock_post):
        mock_resp = None
        mock_post.return_value = mock_resp
        mock_post.side_effect = RequestException()

        result = pmap_service.retrieve_probability_map(area_name, hemisphere, threshold)
        self.assertEqual(result, None)


if __name__ == '__main__':
    main()
