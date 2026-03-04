from django.contrib import admin
from django.urls import path
from core.views import hola

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hola),
]
