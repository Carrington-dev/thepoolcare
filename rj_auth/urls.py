from django.contrib import admin
from django.urls import path, include
from rj_auth import views as acc_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',acc_views.home , name='home'),
]