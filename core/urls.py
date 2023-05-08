from django.urls import path
from . import views 

urlpatterns= [

    path("", views.home, name="home"),
    path("new_series", views.new_series, name="series-create"),
    path("new_post", views.new_post, name="post-create"),
    path("<series>", views.series, name="series"),
    path("<series>/update", views.series_update, name="series_update"),
    path("<series>/delete", views.series_delete, name="series_delete"),
    path("<series>/<article>", views.article, name="article"),
    path("<series>/<article>/update", views.article_update, name="article_update"),
    path("<series>/<article>/delete", views.article_delete, name="article_delete"),
    path('<series>/<article>/upload_image', views.upload_image, name="upload_image"),
    path("newsletter", views.newsletter, name="newsletter"),


    #path('home', rincon, name="rincon"),
    #path('registerpage', registerpage, name="registerpage"),
    #path('correo', correo, name="correo"),
    #path('profile', profile, name="profile"),
    #path('recuperar', recuperar, name="recuperar"),
    #path('signin', signin, name="signin"),
    #path('terminos', terminos, name="terminos"),
    #path('testing', testing, name="testing"),
    


]