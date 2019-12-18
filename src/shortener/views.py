from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import KirrURL

# Create your views here.
def test_view(request):
	return HttpResponse("some stuff!!!")

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	return HttpResponseRedirect(obj.url)

def kirr_shortcut_test(request, shortcode=None, *args, **kwargs): #function based view FBV

	#obj = get_object_or_404(KirrURL, shortcode=shortcode) #shortcut doesn't work, I don't know why
	# por causa disso, uso o equivalente
	print('shortcode = ' + shortcode)
	obj = None
	try:	
		obj = KirrURL.objects.get(shortcode=shortcode)
	except KirrURL.DoesNotExist:
		return HttpResponse('shortcode = ' + shortcode, status=404)
		#raise Http404()


	#obj = KirrURL.objects.get(shortcode=shortcode)

		#obj_u"rl = obj.url
	#print("Url: " + obj.url)
	#try:
	#	obj = KirrURL.objects.get(shortcode=shortcode)
	#except:
	#	obj = KirrURL.objects.all().first()

	#obj_url = None
	#qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	#if qs.exists() and qs.count == 1:
	#	obj = qs.first()
	#	obj_url = obj.url

	return HttpResponse("hello {sc}".format(sc=obj.url))

	#return HttpResponseRedirect(obj.url)

class KirrCBView(View): #class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		#obj = get_object_or_404(KirrURL, shortcode=shortcode)
		print('shortcode:' + shortcode)
		obj = KirrURL.objects.get(shortcode=shortcode)
		#return HttpResponse("Hello again {sc}".format(sc=shortcode))
		return HttpResponseRedirect(obj.url)

	def post(self, request, *args, **kwargs):
		return HttpResponse()

'''
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
	#print(request.user)
	#print(request.user.is_authenticated())

	print('method is \n')
	print(request.method)

	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	#obj_url = obj.url
	#try:
	#	obj = KirrURL.objects.get(shortcode=shortcode)
	#except:
	#	obj= KirrURL.objects.all().first()

	# obj_url = None
	# qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url

	return HttpResponse("hello {sc}".format(sc=obj.url))
'''
