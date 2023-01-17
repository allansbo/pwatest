from django.contrib.auth import get_user_model
from django.test import TestCase
from django.shortcuts import resolve_url as r

User = get_user_model()


class TestTaskListViewForAuthenticatedUser(TestCase):

    def setUp(self):
        self.credentials = dict(username='valentina', password='valentina')
        self.user = User.objects.create_user(**self.credentials)
        self.login = self.client.login(**self.credentials)
        self.response = self.client.get(r('tasks:list'))

    def test_get(self):
        """ GET tasks/read_all/ must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ GET tasks/read_all/ must use task_list.html """
        self.assertTemplateUsed(self.response, 'tasks/task_list.html')


class TestTaskListViewForNonAuthenticatedUser(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(r('tasks:list'))

    def test_get(self):
        """ GET tasks/read_all/ must return status code 302 """
        self.assertEqual(302, self.response.status_code)
