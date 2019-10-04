import random
from django.db import models

# Create your models here.

def code_generator(size=6, chars='abcdefghijklmnopqrstuvwyxz'):
	#new_code = ''
	#for _ in range(size):
	#	new_code += random.choice(chars)
	#return new_code
	return ''.join(random.choice(chars) for_ in range(size))


class KirrURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True)
	updated = models.DateTimeField(auto_now=True) #everytime the is saved
	timestamp = models.DateTimeField(auto_now_add=True) #when model was created
	empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=True) 
	#shortcode = models.CharField(max_length=15, null=True) Empty in database is okay
	#shortcode = models.CharField(max_length=15, default='defaultshortcode')

	def save(self, *args, **kwargs):
		print('something')
		self.shortcode = code_generator()
		super(KirrURL, self).save(*args, **kwargs)

	#def my_save(self):
	#	self.save()

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

'''
Sempre que alterar, execute
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''		