from django.shortcuts import render
from.models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from  django.shortcuts import get_object_or_404
import datetime



# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()

    return render(request, "registros/principal.html",{"9B":alumnos})
#Indicamos el lugar se redenrizara

def registrar(request):
    if request.method =='POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
        comentarios = ComentarioContacto.objects.all() 
        return render(request,"registros/comentario.html", {'comentario':comentarios})

    form = ComentarioContactoForm()
#Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})
    
    
def Contacto(request):
    return render(request,"registros/contacto.html")


def comentario(request):
   comentario = ComentarioContacto.objects.all()
   return render(request, "registros/comentario.html",{"comentario":comentario})



def eliminarComentarioContacto(request,id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario =  get_object_or_404(ComentarioContacto,id=id)
    if request.method =="POST":
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request,"registros/contacto.html",{"comentarios": comentarios})
    return render(request,confirmacion,{"object":comentario})

def consultarComentarioIndivivual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formularioeditar.html", {'comentario':comentario})

def editarComentarioContacto(request,id):
    comentario =  get_object_or_404(ComentarioContacto,id=id)
    form = ComentarioContactoForm(request.POST,instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/contacto.html",{'comentario':comentarios})
        
    return render(request,"registros/formularioeditar.html",{'comentario':comentario})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html",{'9B': alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="MATUTINO")
    return render(request, "registros/consultas.html",{'9B': alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request, "registros/consultas.html",{'9B': alumnos})
    
def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="VESPERTINO")
    return render(request,"registros/consultas.html",{'9B':alumnos})


def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["AD", "MARY"])
    return render(request,"registros/consultas.html",{'9B':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2024, 8,6)
    fechaFin = datetime.date(2024, 8, 11)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'9B':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains="no escrito")
    return render(request, "registros/consultas.html",{'9B': alumnos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'9B':alumnos})



   








