from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from core.tasks.forms import TaskForm
from core.tasks.models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    form = TaskForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'Tarefa adicionada com sucesso')
            return HttpResponseRedirect(r('tasks:list'))
        else:
            messages.warning(request, 'Corrija os campos em destaque')

    context = {'form': form}
    return render(request, 'tasks/task_form.html', context)


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'status']
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks:list')


@login_required
def task_delete(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'A tarefa foi removida')
        return HttpResponseRedirect(r('tasks:list'))

    return render(request, 'tasks/task_delete.html', context)
