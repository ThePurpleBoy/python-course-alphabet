from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.urls import reverse
from .mixins import FormMessageMixin
from .models import Article
from .forms import ArticleForm
from account.models import Profile
from comments.models import Comment


class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'All titles'
        return context


class ArticleCreateView(FormMessageMixin, CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm
    form_valid_message = 'Article created successfully!'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super(ArticleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDetailView(DetailView, MultipleObjectMixin):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        article_id = self.kwargs['article_id']
        article = Article.objects.get(pk=article_id)
        object_list = Comment.objects.filter(article=article)
        context = super(ArticleDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class ArticleUpdateView(FormMessageMixin, UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    pk_url_kwarg = 'article_id'
    form_valid_message = 'Updated successfully!'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/'
    pk_url_kwarg = 'article_id'
    template_name = 'article/confirm_delete.html'
    context_object_name = 'article'
