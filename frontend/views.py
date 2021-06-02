from django.shortcuts import render

# Create your views here.
# renders the index template, then allows react to take over the template


def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
