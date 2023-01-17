from django.contrib.auth import get_user_model
from django.test import TestCase
from django.shortcuts import resolve_url as r

from myDjangoProject.tasks.forms import TaskForm
from myDjangoProject.tasks.models import Task

User = get_user_model()


class TestViewCreateTask(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(r('tasks:create'))

    def test_get(self):
        """ GET tasks/create/ must return status code 200 """
        self.assertTrue(200, self.response.status_code)

    def test_template(self):
        """ Must use task_form.html """
        self.assertTemplateUsed(self.response, 'tasks/task_form.html')

    def test_html(self):
        """ HTML must contains input tags """
        tags = (
            ('<form', 2),
            ('<input', 4),
            ('<select', 1),
            ('type="text"', 2),
            ('type="submit"', 1),
            ('type="reset"', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """ HTML must contain csrf_token """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have task form """
        form = self.response.context['form']
        self.assertIsInstance(form, TaskForm)


class TestPostCreateTask(TestCase):
    def setUp(self) -> None:
        self.credentials = dict(username='valentina', password='valentina')
        self.user = User.objects.create_user(**self.credentials)
        self.login = self.client.login(**self.credentials)
        data = dict(title='Comprar ração', status='todo')
        self.response = self.client.post(r('tasks:create'), data)

    def test_post(self):
        """ The valid POST redirects to the tasks list """
        self.assertEqual(302, self.response.status_code)

    def test_redirect(self):
        """ The valid POST must redirect to tasks list """
        self.assertRedirects(self.response, r('tasks:list'))


class TestInvalidPostCreateTask(TestCase):
    def setUp(self) -> None:
        self.response = self.client.post(r('tasks:create'), {})

    def test_post(self):
        """ Invalid POST should not redirect """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Invalid POST must use the same HTML form """
        self.assertTemplateUsed(self.response, 'tasks/task_form.html')

    def test_has_form(self):
        """ The invalid POST must have a form inside him """
        form = self.response.context['form']
        self.assertIsInstance(form, TaskForm)

    def test_dont_save_task(self):
        """ The invalid POST must not save in database """
        self.assertFalse(Task.objects.exists())
