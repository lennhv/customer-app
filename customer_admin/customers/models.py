from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Customer(models.Model):
    name = models.CharField(_('name'), max_length=100)
    address = models.CharField(_('address'), max_length=200)
    creation_at = models.DateTimeField(_('creation at'), auto_now_add=True)

    def __str__(self):
        return self.name
