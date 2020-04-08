# flake8: noqa
from django.urls import path, include
from rest_framework import routers
from .views import (
    SubscriberApiView,
    BlogApiView,
    HomeView,
    ArticlesView,
    subscribeView,
    AboutView,
    DetailArticleView,
    CreateArticleView,
    UpdateArticleView,
    DeleteArticleView,
    user_login,
    user_logout,
)
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('subscriber', SubscriberApiView)
router.register('blog', BlogApiView)

app_name = 'Blog'

urlpatterns = [
    path("api/", include(router.urls)),
    path('', HomeView.as_view(), name="Home"),
    path('subscribe', subscribeView, name="Subscribe"),
    path('who', AboutView.as_view(), name='Who'),
    path('articles', ArticlesView.as_view(), name="Articles"),
    path('article/<slug>/', DetailArticleView.as_view(), name="Article_Detail"),
    path('new', CreateArticleView.as_view(), name="new_Article"),
    path('article/<slug>/edit/', UpdateArticleView.as_view(), name="update_Article"),
    path('article/<slug>/delete/', DeleteArticleView.as_view(), name="delete_Article"),
    path('IamGitau/admin/login', user_login, name='login'),
    path('IamGitau/admin/logout', user_logout, name='logout'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('IamGitau/admin/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('IamGitau/admin/password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('IamGitau/admin/password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('IamGitau/admin/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('IamGitau/admin/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('IamGitau/admin/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_done'),
]
