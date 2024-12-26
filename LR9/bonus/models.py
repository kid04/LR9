from django.db import models
from django.contrib.auth.models import User


class UserLevel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    spend = models.FloatField(db_default=0)
    level = models.ForeignKey('Level', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.user.__str__()

class Level(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
