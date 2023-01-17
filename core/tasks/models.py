from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

STATUS = (
    ('todo', 'À fazer'),
    ('doing', 'Em andamento'),
    ('done', 'Terminado')
)


class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='usuário')
    title = models.CharField('título', max_length=255)
    status = models.CharField('status', max_length=5, choices=STATUS, default='todo')
    start_date = models.DateTimeField('início', auto_now_add=True)
    end_date = models.DateTimeField('fim', null=True, default=None)

    def save(self, *args, **kwargs):
        """
        Override the save method to define a valid end_date
        """
        if self.status == 'done':
            self.end_date = timezone.now()
        else:
            self.end_date = None
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.status} - {self.title}'

    class Meta:
        ordering = ['status', 'start_date']
