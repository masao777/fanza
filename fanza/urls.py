from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('fanza_serch/', include('fanza_serch.urls')),
    path('admin/', admin.site.urls),
]
