from django import forms
from django.utils import timezone

from core.tasks.models import Task

STATUS = (
    ('todo', 'À fazer'),
    ('doing', 'Em andamento'),
    ('done', 'Terminado')
)


class TaskForm(forms.Form):
    title = forms.CharField(max_length=255, label='Título')
    status = forms.ChoiceField(choices=STATUS, label='Status')

    def save(self, user):

        data = self.cleaned_data
        if data['status'] == 'done':
            data['end_date'] = timezone.now()
        else:
            data['end_date'] = None

        task = Task.objects.create(
            title=data['title'], status=data['status'],
            user=user, end_date=data['end_date'])
        task.save()
