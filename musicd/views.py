from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Track, Vote, Comment
from .forms import TrackForm

def index(request):
    tracks = Track.objects.all()
    print(len(tracks))
    return render(request, 'musicd/index.html', { 'tracks_list': tracks })

@login_required
def upload(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save()
            return render(request, 'musicd/upsuccess.html', {'track': track})

    else:
        form = TrackForm()
    return render(request, 'musicd/upload.html', {'form': form})

@login_required
def vote(request):
    if request.method == 'POST':
        # print(request.POST.vote)
        print(request.POST['track'])
        track_id = request.POST['track']
        track = Track.objects.get(pk=track_id)
        vote = request.POST['vote']
        user = request.user
        if 1 <= int(vote) <= 5 and track is not None:
            v = Vote.objects.create(track=track, user=user, vote=vote)
            return render(request, 'musicd/track.html', {'track': track})
        else:
            return HttpResponse('Icorrect Data')

    else:
        return HttpResponse('Incorrect HTTP METHOD')
    return HttpResponse('Vote Falied')

@login_required
def comment(request):
    if request.method == 'POST':
        track_id = request.POST['track']
        track = Track.objects.get(pk=track_id)
        comment = request.POST['comment']
        user = request.user
        if comment and track is not None:
            v = Comment.objects.create(track=track, user=user, comment=comment)
            return render(request, 'musicd/track.html', {'track': track})
        else:
            return HttpResponse('Icorrect Data')
    else:
        return HttpResponse('Incorrect HTTP METHOD')
    return HttpResponse('Comment Falied')
