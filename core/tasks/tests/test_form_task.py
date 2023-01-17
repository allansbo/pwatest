from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestFormTask(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(r('tasks:create'))

    def test_has_fields(self):
        """ Form must have the input fields """
        form = self.response.context['form']
        self.assertEqual(['title', 'status'], list(form.fields))
