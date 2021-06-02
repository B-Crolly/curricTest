from django.urls import path
from .views import index

# this file has the front facing urls for the project(the ones the user will see
#
urlpatterns = [
    path('', index)
]
