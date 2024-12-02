from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'prueba_django_app/home.html')
def servicios(request):
    return render(request, 'prueba_django_app/servicios.html')
def tienda(request):
    return render(request, 'prueba_django_app/tienda.html')
def contacto(request):
    return render(request, 'prueba_django_app/contacto.html')
def blog(request):
    return render(request, 'prueba_django_app/blog.html')