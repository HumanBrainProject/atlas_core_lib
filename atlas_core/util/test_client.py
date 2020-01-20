from unittest import mock, TestCase, main
from unittest.mock import Mock
from requests import RequestException
from atlas_core.util import client

json_header = {'Content-Type': 'application/json'}
base_url = 'http://s2i-java-atlas-core.apps-dev.hbp.eu'
dummy_url = '/dummy-test-url'


def _mock_response(status=200, content="CONTENT"):

    mock_resp = Mock()
    mock_resp.status_code = status
    mock_resp.content = content
    return mock_resp


class TestRequestsCall(TestCase):

    valid_result_data = 'RESULT_DATA'

    @mock.patch('requests.get')
    def test_valid_response(self, mock_get):
        mock_resp = _mock_response(content=self.valid_result_data)
        mock_get.return_value = mock_resp

        result = client.get_call(dummy_url, header=json_header)
        self.assertEqual(result.content, self.valid_result_data)
        self.assertEqual(result.status_code, 200)
        mock_get.assert_called_with(base_url + dummy_url, headers=json_header)

    @mock.patch('requests.get')
    def test_content_not_none_but_wrong_status(self, mock_get):
        mock_resp = _mock_response(content=self.valid_result_data, status=418)
        mock_get.return_value = mock_resp

        result = client.get_call(dummy_url, header=json_header)
        self.assertEqual(result, None)

    @mock.patch('requests.get')
    def test_content_none(self, mock_get):
        mock_resp = None
        mock_get.return_value = mock_resp

        result = client.get_call(dummy_url, header=json_header)
        self.assertEqual(result, None)

    @mock.patch('requests.get')
    def test_requests_throws_exception(self, mock_get):
        mock_resp = None
        mock_get.return_value = mock_resp
        mock_get.side_effect = RequestException()

        result = client.get_call(dummy_url, header=json_header)
        self.assertEqual(result, None)

    @mock.patch('requests.get')
    def test_valid_response_without_base_url(self, mock_get):
        mock_resp = _mock_response(content=self.valid_result_data)
        mock_get.return_value = mock_resp
        url = 'http://my-full-url'
        result = client.get_call(url, without_base_url=True, header=json_header)
        self.assertEqual(result.content, self.valid_result_data)
        self.assertEqual(result.status_code, 200)
        mock_get.assert_called_with(url, headers=json_header)


if __name__ == '__main__':
    main()
