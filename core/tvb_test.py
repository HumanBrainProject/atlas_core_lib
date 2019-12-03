from unittest import TestCase, mock

from mock import Mock

from core import tvb


class TestTvbMethods(TestCase):

    node = 'TEST_NODE'

    mock_value = Mock()
    value = '{"value": "test"}'
    mock_value.decode = lambda encoding: '{"value": "test"}'

    mock_resp = Mock()
    mock_resp.content = mock_value

    @mock.patch('core.util.client.get_call')
    def test_get_all_nodes(self, mock_get_call):
        mock_get_call.return_value = self.mock_resp
        tvb.get_all_nodes()
        mock_get_call.assert_called_with('/brain/dummy/node')

    @mock.patch('core.util.client.get_call')
    def test_all_get_methods(self, mock_get_call):
        mock_get_call.return_value = self.mock_resp

        functions_and_urls = {
            tvb.get_node_information: f'/brain/dummy/node/{self.node}',
            tvb.get_area_for_node: f'/brain/dummy/node/{self.node}/area',
            tvb.get_average_orientation_for_node: f'/brain/dummy/node/{self.node}/average-orientation',
            tvb.get_centre_for_node: f'/brain/dummy/node/{self.node}/centre',
            tvb.get_cortical_for_node: f'/brain/dummy/node/{self.node}/cortical',
            tvb.get_tract_length_for_node: f'/brain/dummy/node/{self.node}/tract-length',
            tvb.get_volume_for_node: f'/brain/dummy/node/{self.node}/volume',
            tvb.get_weights_for_node: f'/brain/dummy/node/{self.node}/weights',
        }

        for f in functions_and_urls:
            f(self.node)
            mock_get_call.assert_called_with(functions_and_urls[f])
