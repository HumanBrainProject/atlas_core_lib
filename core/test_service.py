# from unittest import TestCase, mock
#
# from mock import Mock
#
# from core import service
#
#
# class TestService(TestCase):
#     mock_value = Mock()
#     mock_value.decode = lambda encoding: '{"_embedded": {"referencespaces": [' \
#                                          '{"referencespace":' \
#                                          '{"name":"colin"},"_links":{"self":{"href":"selflink"},' \
#                                          '"parcellations":{"href":"parcellations"}}}, ' \
#                                          '{"referencespace":' \
#                                          '{"name":"MNI152"},"_links":{"self":{"href":"selflink"},' \
#                                          '"parcellations":{"href":"parcellations"}}} ' \
#                                          ']}}'
#     mock_resp = Mock()
#     mock_resp.content = mock_value
#
#     @mock.patch('core.util.client.get_call')
#     def test_get_all_referencespaces(self, mock_get_call):
#         mock_get_call.return_value = self.mock_resp
#         referencespaces = service.get_all_referencespaces()
#         self.assertEqual(len(referencespaces), 2)
#         self.assertEqual(referencespaces[0].name, 'colin')
#
#     @mock.patch('core.util.client.get_call')
#     def test_get_all_referencespaces_http_error(self, mock_get_call):
#         mock_get_call.return_value = None
#         referencespaces = service.get_all_referencespaces()
#         self.assertEqual(len(referencespaces), 0)
#
#     @mock.patch('core.util.client.get_call')
#     def test_get_all_referencespaces_empty_result(self, mock_get_call):
#         self.mock_value.decode = lambda encoding: '{"_embedded": {"referencespaces": []}}'
#         mock_get_call.return_value = self.mock_resp
#         referencespaces = service.get_all_referencespaces()
#         self.assertEqual(len(referencespaces), 0)
#
#     @mock.patch('core.util.client.get_call')
#     def test_get_referencespace_by_name(self, mock_get_call):
#         self.mock_value.decode = lambda encoding: '{"referencespace":{"name":"colin"},' \
#                                                   '"_links":{"self":{"href": "selfink"},' \
#                                                   '"parcellations":{"href":"parcellations"}}}'
#         mock_get_call.return_value = self.mock_resp
#         referencespace = service.get_referencespace_by_name('colin')
#         self.assertEqual(referencespace.name, 'colin')
#
#     @mock.patch('core.util.client.get_call')
#     def test_get_referencespace_by_name_none_on_error(self, mock_get_call):
#         mock_get_call.return_value = None
#         referencespace = service.get_referencespace_by_name('colin')
#         self.assertEqual(referencespace, None)
