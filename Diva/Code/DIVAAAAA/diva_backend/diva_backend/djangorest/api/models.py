# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ModelBase(models.Model):
    """
        This is a abstract model class to add is_deleted, created_at and modified at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class User(ModelBase):
    """
    It is for Use Model
    """
    user_id = models.IntegerField()
    location = models.CharField(max_length=254, null=True, blank=True)


class Book(ModelBase):
    """
    It is for Use Model
    """
    Player = models.CharField(max_length=254, null=True, blank=True)
    Team = models.CharField(max_length=254, null=True, blank=True)
    Age = models.CharField(max_length=254, null=True, blank=True)
