from django.contrib import admin

from core.contacts.models import Contact


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'city']


admin.site.register(Contact, ContactModelAdmin)
