from django.shortcuts import render
from django.utils.translation import gettext as _
from blog.models import Article


# Create your views here.

global_context = {
    'author_name': _('Айдар Исенов')
}


def home_page(request):
    articles = Article.objects.order_by('-pubdate')
    context = global_context | {'articles': articles}
    return render(request, 'blog/home_page.html', context)



def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = global_context | {'article': article}
    return render(request, 'blog/article_page.html', context)
