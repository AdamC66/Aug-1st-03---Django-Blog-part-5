from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article, Comment, CommentForm


def root(request):
    return HttpResponseRedirect('home')


def home(request):
    context = {'date' : datetime.today().strftime('%Y-%m-%d'), 
    'articles': Article.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def article(request, id):
    form = CommentForm(request.POST)
    context = {'article': Article.objects.get(pk=id), 'form': form}
    return render(request, 'article.html', context)


def create_comment(request):    
    article_id = request.POST['article']
    articlelink = Article.objects.filter(id=article_id).first()
    # name = request.POST['name']
    # message = request.POST['message']
    # new_comment = Comment(name=name, message=message, article=articlelink)
    # new_comment.save()
    form = CommentForm(request.POST)
    context = {'article': articlelink, 'form': form}
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.article = articlelink
        form.save()
        return render(request, 'article.html', context)
    else:
        return render(request, 'article.html', context)