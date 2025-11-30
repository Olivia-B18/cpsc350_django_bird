"""Defines URL patterns for bird_logs."""

from django.urls import path

from . import views

app_name = 'bird_logs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # page that shows all birds
    path('birds/', views.birds, name='birds'),

    # details page for single bird
    path('bird/<int:bird_id>/', views.bird, name='bird'),

    # Page for adding a new bird.
    path('new_bird/', views.new_bird, name='new_bird'),

    # Page for adding a new sighting.
    path('new_sighting/<int:bird_id>/', views.new_sighting, name='new_sighting'),

    # Page for editing an sighting.
    path('edit_sighting/<int:sighting_id>/', views.edit_sighting, name='edit_sighting'),

    # Page for editing a bird.
    path('edit_bird/<int:bird_id>/', views.edit_bird, name='edit_bird'),

]
