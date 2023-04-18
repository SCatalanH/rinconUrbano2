from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'core/rinconUrbano.html')

def rincon(request):

    return render(request, 'core/rinconUrbano.html')

def registerpage(request):

    return render(request, 'core/html/register.html')

def articulo(request):

    return render(request, 'core/html/articulo.html')

def correo(request):

    return render(request, 'core/html/correo.html')

def profile(request):

    return render(request, 'core/html/profile.html')

def recuperar(request):

    return render(request, 'core/html/recuperar.html')

def signin(request):

    return render(request, 'core/html/signin.html')

def terminos(request):

    return render(request, 'core/html/terminos.html')

def testing(request):

    return render(request, 'core/html/testing.html')



