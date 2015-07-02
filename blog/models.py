from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(User)
	pub_date = models.DateTimeField('date published', default=datetime.now)
	post_text = models.CharField(max_length=5000)
	post_title = models.CharField(max_length=200, default="")
	published = models.BooleanField(default=False)

	MARKDOWN = 'M'
	HTML = 'H'
	edit_choices = (
		(MARKDOWN, 'Markdown'),
		(HTML, 'HTML'),
	)
	edit_type = models.CharField(max_length=1, choices=edit_choices, default=MARKDOWN)

	def __str__(self):
		return self.post_title