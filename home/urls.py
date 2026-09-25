


from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('projects/', views.projects, name='projects'),

    path('academics/', views.academics, name='academics'),

    path('skills/', views.skills, name='skills'),

    path('achievements/', views.achievements, name='achievements'),

    path('experience/', views.experience, name='experience'),

]