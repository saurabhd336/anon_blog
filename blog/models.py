from django.db import models
from datetime import datetime

class Post(models.Model):
	title = models.CharField(max_length = 300, null = False)
	story = models.CharField(max_length = 10000, null = False)
	publish_date = models.DateTimeField(default = datetime.now());
# Create your models here.

class FileTest(models.Model):
	f = models.FileField( upload_to = 'files/')
