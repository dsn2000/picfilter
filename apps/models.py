from django.db import models

class Pic(models.Model):
	picture = models.ImageField(upload_to='images/')
	
class Filt(models.Model):
	filtered = models.ImageField(upload_to='images/')