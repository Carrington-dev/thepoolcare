from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rj_auth.models import Account

@admin.register(Account)
class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff','is_student','is_teacher')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()