from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    supervisor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username


