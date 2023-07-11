from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Article, Comment, Category
from .forms import ArticleForm, CommentForm


def articles_list(request):
    articles = Article.objects.all()
    categories = Category.objects.all()

    return render(request, 'articles/articles_list.html', {'articles': articles, 
                                                           'categories': categories})


def articles_by_category(request, slug):
    articles = Article.objects.all()
    categories = Category.objects.all()
    category = None
    if slug:
        category = get_object_or_404(Category, slug=slug)
        articles = articles.filter(category=category)
    
    return render(request, 'articles/articles_list.html', {'articles': articles, 
                                                           'category': category,
                                                           'categories': categories})


def articles_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article).order_by('-pk')
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST or None)
            if form.is_valid():
                content = request.POST.get('content')
                comment = Comment.objects.create(article=article, user=request.user, content=content)
                comment.save()
        else:
            return redirect('users:login')
    else:
        form = CommentForm

    return render(request, 'articles/articles_detail.html ', {'article': article, 
                                                              'comments':comments, 
                                                              'form': form})


@login_required()
def articles_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return redirect('articles:list')
    else:
        form = ArticleForm()    
    
    return render(request, 'articles/articles_create.html', {'form': form})