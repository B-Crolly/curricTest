from django.urls import path
from .views import SurveyView
urlpatterns = [
    #if url has no path, run main
    path('survey', SurveyView.as_view())

]