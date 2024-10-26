from django.shortcuts import render, redirect #se impota la redireccion
from appConcierto.models import Concierto #se importa el modelo
from appConcierto.forms import FormConcierto #se importa el formulario
# Create your views here.
def index(request):  #vista index
    return render(request, 'index.html')

def listadoConcierto(request):  #vista listado
    conciertos = Concierto.objects.all
    data = {'conciertos': conciertos}
    return render(request, 'listadoConcierto.html', data)

def agregarConcierto(request):
    form = FormConcierto()
    if request.method == 'POST':
        form = FormConcierto(request.POST)
        if form.is_valid():
            form.save()
            return index (request)
    else:
        form = FormConcierto()
    data = {'form':form}
    return render(request, 'agregarConcierto.html', data)

def actualizarConcierto(request, id):
    concierto = Concierto.objects.get(id = id)
    form = FormConcierto(instance=concierto)
    if request.method == 'POST':
        form = FormConcierto(request.POST, instance=concierto)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = FormConcierto(instance=concierto)    
    data = {'form':form}
    return render(request, 'agregarConcierto.html', data)

def eliminarConcierto(request, id):
    proyecto = Concierto.objects.get(id=id)
    proyecto.delete()
    return redirect('/conciertos')