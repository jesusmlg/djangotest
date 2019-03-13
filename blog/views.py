from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm

from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

# Create your views here.

class ArticleListView(ListView):
  template_name = 'blog/article_list.html'
  queryset = Article.objects.all()

class ArticleDetailView(DetailView):
  #template_name = 'blog/article_detail.html'
  queryset = Article.objects.all()

# def article_list_view(request):
#   queryset = Article.objects.all()
#   context = {
#     'object_list' : queryset
#   }

#   return render(request, 'article_list.html', context)

# def article_detail_View(request):
#   pass