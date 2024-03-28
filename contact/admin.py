from django.contrib import admin
from contact.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('name', 'email', 'subject', 'message', 'date_sent', 'viewed')
    list_filter = ('name','email',)
    
    readonly_fields = ('email',)
    search_fields = ('email','name',)
    date_hierarchy = 'date_sent'
    ordering = ('-pk',)