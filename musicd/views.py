from django.shortcuts import render
from django.http import HttpResponse

from .models import Track
from .forms import TrackForm

def index(request):
    tracks = Track.objects.all()
    print(len(tracks))
    return render(request, 'musicd/index.html', { 'tracks_list': tracks })

def upload(request):
    print(request.method)
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save()
            return render(request, 'musicd/upsuccess.html', {'track': track})

    else:
        form = TrackForm()
    return render(request, 'musicd/upload.html', {'form': form})

