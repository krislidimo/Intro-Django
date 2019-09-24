from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User # Djangos built in user model

# Create your models here.

class Note(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid4, # automatically populate
		editable=False # not editable
	)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True) # auto_now_add only sets on create
	last_modified = models.DateTimeField(auto_now=True) # auto_now sets on create & update

class PersonalNote(Note):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)