from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DeleteView
from .models import Song
from .forms import UploadForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def home(request):
    songs = Song.objects.all()
    paginator = Paginator(songs, 5)# number of songs displayed on the screen
    page = request.GET.get('page')
    songs =paginator.get_page(page)
    return render(request, 'home.html', {'songs': songs})

def registerpage(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + 'your account is Created')
            return redirect('login')
    return render(request, 'register.html', context)
def loginpage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def upload_song(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage after successful upload
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})
class MusicSearch(ListView):
    model = Song
    template_name = 'home.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Song.objects.filter(Q(title__icontains =query))
        return results


def download_song(request, song_id):
    song = Song.objects.get(id=song_id)
    file_path = song.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='audio/mp3')
        response['Content-Disposition'] = 'attachment; filename=' + song.title + '.mp3'
        return response
    
def delete_song(request, song_id):
    songs = get_object_or_404(Song, id=song_id)
    # Delete the song (which will also delete the associated file)
    songs.delete()
    return redirect('home')  # Redirect to a view or page
 

    