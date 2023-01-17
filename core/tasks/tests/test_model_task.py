from django.contrib.auth import get_user_model
from django.test import TestCase

from myDjangoProject.tasks.models import Task

User = get_user_model()


class TestModelTask(TestCase):
    def setUp(self) -> None:
        self.credentials = dict(username='valentina', password='valentina')
        self.user = User.objects.create_user(**self.credentials)
        self.login = self.client.login(**self.credentials)
        self.obj = Task.objects.create(
            user=self.user,
            title='example',
            status=3
        )

    def test_create(self):
        """ Test must have a task """
        self.assertTrue(Task.objects.exists())

    def test_user_id_cannot_be_null(self):
        """ The user_id cannot be null """
        field = Task._meta.get_field('user_id')
        self.assertFalse(field.null)

    def test_user_id_cannot_be_blank(self):
        """ The user_id cannot be blank """
        field = Task._meta.get_field('user_id')
        self.assertFalse(field.blank)

    def test_end_date_can_be_null(self):
        """ The field end_date can be null """
        field = Task._meta.get_field('end_date')
        self.assertTrue(field.null)

    def test_end_date_cannot_be_blank(self):
        """ The field end_date cannot be blank """
        field = Task._meta.get_field('end_date')
        self.assertFalse(field.blank)

