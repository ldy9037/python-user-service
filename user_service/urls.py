from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
import user.views
import certification.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user.views.list_insert_users, name='list-insert-users'),
    path('cert/', certification.views.request_certification_number, name='request-certification-number')
]
