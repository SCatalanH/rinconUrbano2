from django.urls import URLPattern, path
from .views import home, rincon, registerpage, articulo, correo, profile, recuperar, signin, terminos, testing


urlpatterns= [
    path('', home, name="home"),
    path('home', rincon, name="rincon"),
    path('registerpage', registerpage, name="registerpage"),
    path('articulo', articulo, name="articulo"),
    path('correo', correo, name="correo"),
    path('profile', profile, name="profile"),
    path('recuperar', recuperar, name="recuperar"),
    path('signin', signin, name="signin"),
    path('terminos', terminos, name="terminos"),
    path('testing', testing, name="testing"),
]