from django.urls import path
from . import views 

urlpatterns= [

    path("", views.home, name="home"),
    path("<series>", views.series, name="series"),
    path("<series>/<article>", views.article, name="article"),

    #path('home', rincon, name="rincon"),
    #path('registerpage', registerpage, name="registerpage"),
    #path('correo', correo, name="correo"),
    #path('profile', profile, name="profile"),
    #path('recuperar', recuperar, name="recuperar"),
    #path('signin', signin, name="signin"),
    #path('terminos', terminos, name="terminos"),
    #path('testing', testing, name="testing"),
    


]