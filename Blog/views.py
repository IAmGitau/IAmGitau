from django.contrib import messages
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
from rest_framework import viewsets
from .serializers import SubscriberSerializer, BlogSerializer
from .models import Blog, Subscribers
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileAuthenticationForm, SubForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class BlogApiView(viewsets.ModelViewSet):
    """
    BlogApiView Handle blog Api
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class SubscriberApiView(viewsets.ModelViewSet):
    """
    SubscriberApiView Handle subscribers Api
    """
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer


class HomeView(ListView):
    """
    HomeView:: Show index page
    """
    template_name = "Blog/Index.html"
    model = Blog
    # context_object_name = 'articles'
    extra_context = {
        'articles': Blog.objects.order_by('-created_at')[:5],
        '100days': Blog.objects.order_by('-created_at').filter(label__icontains="100DaysOfCode")[:5],
        'challenges': Blog.objects.order_by('-created_at').filter(label__icontains="CodeChallenges")[:5],
    }


class ArticlesView(ListView):
    """
    ArticlesView:: Show all article
    """
    template_name = 'Blog/Articles.html'
    model = Blog
    context_object_name = 'articles'
    ordering = ['-created_at']


def subscribeView(request):
    """
    ConfirmView:: Confirm subscription page
    """
    if request.method == 'POST':
        form = SubForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, f"Thanks for subscribing")
            return redirect(to='Blog:Home')

        else:
            messages.add_message(request, messages.ERROR, f"Email is taken.")
            return redirect(to='Blog:Subscribe')

    form = SubForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'Blog/Subscribe.html', context)


class AboutView(TemplateView):
    """
    AboutView:: About Page
    """
    template_name = 'Blog/About.html'


class DetailArticleView(DetailView):
    model = Blog
    template_name = 'Blog/Detail.html'
    articleRange = [1, 2, 3]
    extra_context = {
        "articleRange": articleRange
    }


class CreateArticleView(LoginRequiredMixin, CreateView):
    from .forms import NewBlogForm
    model = Blog
    form_class = NewBlogForm

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)


class UpdateArticleView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    from .forms import NewBlogForm
    model = Blog
    form_class = NewBlogForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.Author = self.request.user
            return super().form_valid(form)

    def test_func(self):
        article = self.get_object()  # current article being edited
        if self.request.user.is_authenticated:
            return True
        return False


class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    articleRange = [1, 2, 3]
    extra_context = {
        "articleRange": articleRange
    }
    success_url = '/'

    def test_func(self):
        article = self.get_object()  # current article being edited
        if self.request.user.is_authenticated:
            return True
        return False


def user_login(request):
    """
    :param request:
    :return:
    """
    if request.method == 'POST':
        print("Mull")
        form = ProfileAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            current_user_login = authenticate(username=username, password=password)

            if current_user_login is not None:
                login(request, current_user_login)
                return redirect(to='Blog:Who')
            else:
                return redirect(to='Blog:login')

    form = ProfileAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'Blog/login.html', context)


@login_required
def user_logout(request):
    """
    :param request:
    :return:
    """
    logout(request)
    return redirect(to="Blog:Home")
