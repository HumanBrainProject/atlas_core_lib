from unittest import TestCase, mock
from unittest.mock import Mock

from ebrains_atlascore import allan


class TestAllanMethods(TestCase):

    @mock.patch('ebrains_atlascore.util.client.get_call')
    def test_get_structure(self, mock_get_call):
        def mock_decode(encoding):
            return '{"value": "test"}'
        mock_value = Mock()
        mock_value.decode = mock_decode
        mock_resp = Mock()
        mock_resp.content = mock_value
        mock_get_call.return_value = mock_resp

        data = allan.get_structure()

        self.assertEqual(data['value'], 'test')
