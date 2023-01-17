from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestViewListContacts(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(r('contacts:list'))

    def test_get(self):
        """ GET /contacts/read_all/ must return status code 200 """
        self.assertTrue(200, self.response.status_code)

    def test_template(self):
        """ Must use contact_list.html """
        self.assertTemplateUsed(self.response, 'contacts/contact_list.html')
