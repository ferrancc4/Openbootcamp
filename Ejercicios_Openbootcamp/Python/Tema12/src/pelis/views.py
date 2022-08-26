from django.shortcuts import render, get_object_or_404
from .models import Director, Pelicula


def IndexView(request):
    queryset = Director.objects.all()
    context = {
        'directores_list': queryset
    }
    return render(request, "directores.html", context)

def DirectorView(request, id):
    direct = get_object_or_404(Director, id=id)
    pel_dir = Pelicula.objects.filter(director= direct)
    context ={
        "persona": direct,
        "peliculas": pel_dir
    }
    return render(request, "director.html", context)

def PeliculaView(request, id):
    peli = Pelicula.objects.get(id=id)
    context = {
        "object": peli
    }
    return render(request, "pelicula.html", context)