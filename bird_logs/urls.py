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

    # Page for adding a new entry.
    path('new_entry/<int:bird_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
