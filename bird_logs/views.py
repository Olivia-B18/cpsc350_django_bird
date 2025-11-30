from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Bird, Entry
from .forms import BirdForm, EntryForm

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
    """Show a single bird and all its entries."""
    bird = Bird.objects.get(id=bird_id)
    # Make sure the bird belongs to the current user.
    if bird.owner != request.user:
        raise Http404

    entries = bird.entry_set.order_by('-date_added')
    context = {'bird': bird, 'entries': entries}
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
def new_entry(request, bird_id):
    """Add a new entry for a particular bird."""
    bird = Bird.objects.get(id=bird_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.bird = bird
            new_entry.save()
            return redirect('bird_logs:bird', bird_id=bird_id)

    # Display a blank or invalid form.
    context = {'bird': bird, 'form': form}
    return render(request, 'bird_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    bird = entry.bird
    if bird.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bird_logs:bird', bird_id=bird.id)

    context = {'entry': entry, 'bird': bird, 'form': form}
    return render(request, 'bird_logs/edit_entry.html', context)
