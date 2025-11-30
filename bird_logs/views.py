from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Bird, Sighting
from .forms import BirdForm, SightingForm

def index(request):
    """the home page for Bird Log."""
    return render(request, 'bird_logs/index.html')

@login_required
def birds(request):
    """show all birds"""
    sort = request.GET.get('sort', 'alphabetical')
  
    # sort by date_added
    if sort == 'date_added':
        birds = Bird.objects.filter(owner=request.user).order_by('-date_added')
    # sort by alphabetical order (default)
    else:
        birds = Bird.objects.filter(owner=request.user).order_by('text')
  
    context = {'birds': birds, 'current_sort': sort}
    return render(request, 'bird_logs/birds.html', context)

@login_required
def bird(request, bird_id):
    """Show a single bird and all its sightings."""
    bird = Bird.objects.get(id=bird_id)
    # Make sure the bird belongs to the current user.
    if bird.owner != request.user:
        raise Http404

    sightings = bird.sighting_set.order_by('-sighting_date')
    context = {'bird': bird, 'sightings': sightings}
    return render(request, 'bird_logs/bird.html', context)

@login_required
def new_bird(request):
    """Add a new bird."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BirdForm()
    else:
        # POST data submitted; process data.
        form = BirdForm(data=request.POST)
        if form.is_valid():
            new_bird = form.save(commit=False)
            new_bird.owner = request.user
            new_bird.save()
            return redirect('bird_logs:birds')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'bird_logs/new_bird.html', context)

@login_required
def new_sighting(request, bird_id):
    """Add a new sighting for a particular bird."""
    bird = Bird.objects.get(id=bird_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = SightingForm()
    else:
        # POST data submitted; process data.
        form = SightingForm(data=request.POST)
        if form.is_valid():
            new_sighting = form.save(commit=False)
            new_sighting.bird = bird
            new_sighting.save()
            return redirect('bird_logs:bird', bird_id=bird_id)

    # Display a blank or invalid form.
    context = {'bird': bird, 'form': form}
    return render(request, 'bird_logs/new_sighting.html', context)

@login_required
def edit_sighting(request, sighting_id):
    """Edit an existing sighting."""
    sighting = Sighting.objects.get(id=sighting_id)
    bird = sighting.bird
    if bird.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current sighting.
        form = SightingForm(instance=sighting)
    else:
        # POST data submitted; process data.
        form = SightingForm(instance=sighting, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bird_logs:bird', bird_id=bird.id)

    context = {'sighting': sighting, 'bird': bird, 'form': form}
    return render(request, 'bird_logs/edit_sighting.html', context)

@login_required
def edit_bird(request, bird_id):
    """Edit a bird's details."""
    bird = Bird.objects.get(id=bird_id)
    if bird.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current bird.
        form = BirdForm(instance=bird)
    else:
        # POST data submitted; process data.
        form = BirdForm(instance=bird, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bird_logs:bird', bird_id=bird.id)

    context = {'bird': bird, 'form': form}
    return render(request, 'bird_logs/edit_bird.html', context)
