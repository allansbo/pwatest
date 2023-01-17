from django.contrib.auth import get_user_model
from django.test import TestCase
from django.shortcuts import resolve_url as r

from myDjangoProject.tasks.models import Task

User = get_user_model()


class TestViewDeleteTask(TestCase):
    def setUp(self) -> None:
        self.credentials = dict(username='valentina', password='valentina')
        self.user = User.objects.create_user(**self.credentials)
        self.login = self.client.login(**self.credentials)
        self.obj = Task.objects.create(
            user=self.user,
            title='example',
            status=3
        )
        self.response = self.client.get(r(f'tasks:delete/{self.obj.id}'))

    def test_get(self):
        """ GET /tasks/delete/ must return status code 200 """
        self.assertTrue(200, self.response.status_code)
