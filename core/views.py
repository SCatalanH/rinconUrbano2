from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleSeries

# Create your views here.
def home(request):
    matching_series = ArticleSeries.objects.all()
    
    return render(
        request=request,
        template_name='core/rinconUrbano.html',
        context={"objects": matching_series}
        )

def series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).all()
    
    return render(
        request=request,
        template_name='core/html/series.html',
        context={"objects": matching_series}
        )

def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()
    
    return render(
        request=request,
        template_name='core/html/article.html',
        context={"object": matching_article}
        )


##############################suspendido por mientras#########################

#def rincon(request):

   # matching_series = ArticleSeries.objects.all()

    #return render(request=request,
                 # template_name='core/rinconUrbano.html',
                  #context={"objects": matching_series}
                  
#def registerpage(request):

   # return render(request, 'core/html/register.html')

#def article(request):

    #return render(request, 'core/html/article.html')

#def correo(request):

   # return render(request, 'core/html/correo.html')

#def profile(request):

    #return render(request, 'core/html/profile.html')

#def recuperar(request):

    #return render(request, 'core/html/recuperar.html')

#def signin(request):

    #return render(request, 'core/html/signin.html')

#def terminos(request):

    #return render(request, 'core/html/terminos.html')

#def testing(request):

   # return render(request, 'core/html/testing.html')
###################################

