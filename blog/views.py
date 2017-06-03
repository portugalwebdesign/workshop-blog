from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Article


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        comment_form = CommentForm(initial={'article': article})

    return render(request, 'blog/article/detail.html', {
        'article': article,
        'comment_form': comment_form
    })
