from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Services(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    STATUS = (
        (0, _('Don\'t activate')),
        (1, _('Activate')),
    )
    activation = models.PositiveSmallIntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.user.username


