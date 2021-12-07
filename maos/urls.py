from django.urls import path

from . import views

from maos.admin import admin_site

urlpatterns = [
    path('', views.index, name='index'),
    path('myadmin/', admin_site.urls),
]

