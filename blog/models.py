from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(User)
	pub_date = models.DateTimeField('date published')
	post_text = models.CharField(max_length=5000)
	post_title = models.CharField(max_length=200, default="")