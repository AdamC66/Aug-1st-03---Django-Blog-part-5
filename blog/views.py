from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article, Comment

def root(request):
    return HttpResponseRedirect('home')

def home(request):
    context = {'date' : datetime.today().strftime('%Y-%m-%d'), 
    'articles': Article.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def article(request, id):
    context = {'article': Article.objects.get(pk=id)} 
    return render(request,'article.html', context)

def create_comment(request):
    article_id = request.POST['article']

    articlelink = Article.objects.filter(id=article_id).first()
    name = request.POST['name']
    message = request.POST['message']

    new_comment = Comment(name=name, message=message, article=articlelink)
    new_comment.save()

    context = {'article': articlelink}
    return render(request,'article.html', context)