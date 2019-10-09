from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.

class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(KirrURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=False)
		return qs

	def refresh_shortcodes(self):
		qs = KirrURL.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_codes += 1
		return "New codes made: {i}".format(i=new_codes)

class KirrURL(models.Model):
	url       = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, default='abc', unique=True, blank=True)
	updated   = models.DateTimeField(auto_now=True) #everytime the is saved
	timestamp = models.DateTimeField(auto_now_add=True) #when model was created
	active    = models.BooleanField(default=True)
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=True) 
	#shortcode = models.CharField(max_length=15, null=True) Empty in database is okay
	#shortcode = models.CharField(max_length=15, default='defaultshortcode')

	objects = KirrURLManager()
	#some_random = KirrURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode= create_shortcode(self)
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