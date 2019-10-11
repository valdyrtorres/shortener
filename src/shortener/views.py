from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
	#print(request.user)
	#print(request.user.is_authenticated())
	return HttpResponse("hello {sc}".format(sc=shortcode))

class KirrCBView(View): #class based view
	def get(self, reuest, shortcode=None, *args, **kwargs):
		return HttpResponse("Hello again {sc}".format(sc=shortcode))