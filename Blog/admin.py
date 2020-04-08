from django.contrib import admin
from .models import Subscribers,Blog

admin.site.register(Subscribers)
admin.site.register(Blog)

admin.site.site_header = 'IamGitau Blog'
admin.site.site_title = 'IamGitau Blog'
admin.site.index_title = 'IamGitau Blog'
