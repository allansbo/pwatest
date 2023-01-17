from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, get_object_or_404
from django.views.generic import ListView

from core.contacts.forms import ContactForm
from core.contacts.models import Contact

contact_list = ListView.as_view(model=Contact)


@login_required
def contact_create(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato adicionado com sucesso')
            return HttpResponseRedirect(r('contacts:list'))
        else:
            messages.warning(request, 'Corrija os campos em destaque')

    context = {'form': form}
    return render(request, 'contacts/contact_form.html', context)


@login_required
def contact_delete(request, pk: int):
    contact = get_object_or_404(Contact, pk=pk)
    context = {'contact': contact}

    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'O contato foi removido')
        return HttpResponseRedirect(r('contacts:list'))

    return render(request, 'contacts/contact_delete.html', context)


@login_required
def contact_update(request, pk: int):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Contato atualizado com sucesso')
            return HttpResponseRedirect(r('contacts:list'))
        else:
            messages.warning(request, 'Corrija os campos em destaque')

    context = {'contact': contact, 'form': form}
    return render(request, 'contacts/contact_update.html', context)
