# flake8: noqa
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .utils import readTime


class Blog(models.Model):
    """
    Blog model
    """
    py = 'Python'
    topics = [
        (py, "Python"),
        ("javascript", "javascript  "),
        ("vue js", "vue js"),
        ("Express js", "Express js"),
        ("Laravel", "Laravel"),
        ("Flutter", "Flutter"),
        ("Django", "Django"),
        ("Es6", "Es6"),
        ("IDEs", "IDEs"),
        ("node js", "node js"),
    ]
    noLabel = 'noLabel'
    labels = [
        (noLabel, 'noLabel'),
        ("100DaysOfCode", "100DaysOfCode"),
        ("CodeChallenges", "CodeChallenges"),
    ]
    Title = models.CharField(max_length=2000, null=False, blank=False, help_text='Article title is required',
                             unique=True)
    Author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    Body = models.TextField(blank=False, null=False, help_text='Input blog body')
    slug = models.SlugField(max_length=200, null=False, blank=False, help_text='Article slug is required', unique=True)
    created_at = models.DateTimeField(_('created at'), default=timezone.now)
    tag = models.CharField(max_length=200, blank=False, null=False, choices=topics, default=py)
    label = models.CharField(max_length=200, blank=False, null=False, choices=labels, default=noLabel)

    def __str__(self):
        return self.Title

    def latest(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=.2)

    def get_absolute_url(self):
        return reverse('Blog:Article_Detail', kwargs={'slug': self.slug})

    def read(self):
        return readTime(self.Body)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _("Blog's")


class Subscribers(models.Model):
    """
    Subscribers model
    """
    Email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.Email

    def clean(self):
        super().clean()
        self.Email = self.normalize_email(self.Email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        from django.core.mail import send_mail
        send_mail(subject, message, from_email, [self.Email], **kwargs)

    @classmethod
    def normalize_email(cls, Email):
        """
        Normalize the email address by lower casing the domain part of it.
        """
        email = Email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name + '@' + domain_part.lower()
        return email

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')
