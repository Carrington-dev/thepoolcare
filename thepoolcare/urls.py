from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "Stemgon Softwares"
admin.site.site_title = "The Pool Care"
admin.site.index_title = "The Pool Care welcomes you!!!"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("rj_auth.urls"))
]
