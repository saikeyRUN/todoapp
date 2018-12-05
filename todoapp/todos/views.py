from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse

from .models import Todo , Users

@login_required
def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)
@login_required
def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

@login_required
def add(request):
    #todoid = Todo.objects.get(id=id)
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()
        #context = { 'todoid' : todoid}
        return render (request, 'details.html' ,)
    else:
        return render(request, 'add.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Users.objects.filter(user=request.user)
                todos = Todo.objects.all()[:10]

                context = {
                    'todos': todos
                }
                return render(request, 'index.html', context, {'albums': albums})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

'''def logout_user(request):
    #logout(request)
    #form = UserForm(request.POST or None)
   # context = {
        #"form": form,
    #}
    return redirect('/^$') '''

def register(request):
    #form = UserForm(request.POST or None)
    #if form.is_valid():
        #user = form.save(commit=False)
        #username = form.cleaned_data['username']
        #password = form.cleaned_data['password']
        #user.set_password(password)
        #user.save()
        #user = authenticate(username=username, password=password)
        #if user is not None:
            #if user.is_active:
                #login(request, user)
                #albums = Album.objects.filter(user=request.user)
                #return render(request, 'music/index.html', {'albums': albums})
    context = {
        #"form": form,
    }
    #return render(request, 'music/register.html', context)

"""def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        #albums = Album.objects.filter(user=request.user)
        #song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            #albums = albums.filter(
                #Q(album_title__icontains=query) |
                #Q(artist__icontains=query)
            #).distinct()
            #song_results = song_results.filter(
                #Q(song_title__icontains=query)
            #).distinct()
            return render(request, 'music/index.html', {
                #'albums': albums,
                #'songs': song_results,
            })
        #else:
            #return render(request, 'music/index.html', {'albums': albums}) """