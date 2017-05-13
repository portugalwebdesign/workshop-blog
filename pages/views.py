from django.shortcuts import render

from blog.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'pages/home.html', {'articles': articles})
