from django.db import models
from datetime import datetime

def get_current_date_time():
		return datetime.now()

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	projects = models.ManyToManyField("projects.Project", verbose_name="Related Projects", blank=True)
	tags = models.ManyToManyField("Tag")
	date_created = models.DateTimeField(primary_key=True, default=get_current_date_time)
	last_modified = models.DateTimeField(auto_now=True)
	content = models.TextField()

	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=50, primary_key=True)

	def __str__(self):
		return self.name