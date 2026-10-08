from django.shortcuts import render,redirect,get_object_or_404
from.models import autor,libro

def crearAutor(request):
    if request.method == 'GET':
        return render(request,'crearAutor.html')
    else:
        autorObj = autor(
            nombre= request.POST.get('nombre'),
            lugar_nacimiento=request.POST.get('lugar'),
            fecha_nacimiento = request.POST.get('fecha')
        )
        autorObj.save()
        return redirect('crearAutor')
        

def editarAutor(request, autor_id):
    if request.method == "GET":
        autorObj = get_object_or_404(autor,pk=autor_id)
        return render(request,'editarAutor.html',{'autores':autorObj})
    else:
        autorObj = get_object_or_404(autor,pk=autor_id)
        autorObj.nombre = request.POST.get('nombre')
        autorObj.lugar_nacimiento = request.POST.get('lugar')
        autorObj.fecha_nacimiento = request.POST.get('fecha')
        
        autorObj.save()
        return redirect('crearAutor')
    
    
def eliminarAutor(request, autor_id):
    autorObj = get_object_or_404(autor,pk=autor_id)
    autorObj.delete()
    return redirect('crearAutor')
def crearLibro(request):
    if request.method == 'GET':
        autores = autor.objects.all()
        return render(request,'crearLibro.html',{'autores':autores})
    else:
        autorObj = get_object_or_404(autor, pk=request.POST.get('autor'))
        libroObj = libro(
            titulo = request.POST.get('titulo'),
            descripcion = request.POST.get('descripcion'),
            autor_id = autorObj
        )
        libroObj.save()
        return redirect('crearLibro')
    
def listarLibros(request):
    libros =libro.objects.all()
    return render(request,'listarLibros.html',{'libros':libros})

def editarLibro(request,libro_id):
    if request.method == "GET":
        LibroObj = get_object_or_404(libro,pk=libro_id)
        autores = autor.objects.all()
        return render(request,'editarLibro.html',{
            'libro':LibroObj,
            'autores':autores})
    else:
        LibroObj = get_object_or_404(libro,pk=libro_id)
        autorObj = get_object_or_404(autor,pk= request.POST.get('autor'))
        LibroObj.titulo = request.POST.get('titulo')
        LibroObj.descripcion = request.POST.get('descripcion')
        LibroObj.autor = autorObj
        LibroObj.save()
        return redirect('listarlibros')
    
def eliminarLibro(request,libro_id):
    libroObj = get_object_or_404(libro,pk =libro_id)
    libroObj.delete()
    return redirect('listarlibros')

def listarAutores(request):
    autores = autor.objects.all()
    return render(request, 'listarAutores.html', {'autores':autores})



