from __future__ import unicode_literals

from django.db import models

from ..login_reg.models import User

class snackManager(models.Manager):

    def snack_request(self,snack_request, id):
        self.create(snack_request=snack_request, user=id)
        return (self, True)

# Create your models here.
class Snack(models.Model):
    snack_request = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    SnackManager = snackManager()
