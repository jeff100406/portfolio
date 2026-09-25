

from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def projects(request):
    return render(request, 'home/projects.html')


def academics(request):
    return render(request, 'home/academics.html')


def skills(request):
    return render(request, 'home/skills.html')


def achievements(request):
    return render(request, 'home/achievements.html')


def experience(request):
    return render(request, 'home/experience.html')

# Create your views here.
